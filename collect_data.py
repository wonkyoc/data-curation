from datasets import load_dataset
import json
import os.path

datasets = {
        #"wiki": "olm/wikipedia",           # works
        #"pg19": "deepmind/pg19",           # 
        #"owt2": "segyges/OpenWebText2",    # 
        #"pol": "pile-of-law/pile-of-law"   # works
        "minipile": "JeanKaddour/minipile"  # works
        }


def load_data(k, v):
    #cache_dir = "/p/alpha/hf_cache"
    if k == "wiki":
        return load_dataset(v, language="en", date="20240601")
    elif k == "pol":
        return load_dataset(v, "all")
    else:
        return load_dataset(v)


def main():
    for k, v in datasets.items():
        print(f"create {k}")
        if os.path.exists(f"data/{k}.jsonl"):
            print(f"{k} exists")
            continue
        d = load_data(k, v)

        texts = []
        for row in d["train"]:
            text = ""
            for k, v in row.items():
                text += f"{k}: {v}"
            texts.append({"text": text})
        
        # write concat jsonl
        with open(f"data/{k}.jsonl", "w") as f:
            for row in texts:
                f.write(json.dumps(row) + "\n")

if __name__ == "__main__":
    main()
