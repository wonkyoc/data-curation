from datasets import load_dataset
import json
import os.path

datasets = {
        #"wiki": "olm/wikipedia",           # works
        #"pg19": "deepmind/pg19",           # 
        #"owt2": "segyges/OpenWebText2",    # 
        #"pol": "pile-of-law/pile-of-law"   # works
        #"minipile": "JeanKaddour/minipile"  # works
        "test": None,
        "demo": None,
        }



def combine_data():
    lines = []
    for k, v in datasets.items():
        filename = f"data/{k}.jsonl"
        if os.path.exists(filename) == False:
            assert(f"{k}.jsonl not exist")
        with open(filename, "r") as f:
            chunk = f.read().split("\n")
            for line in chunk[:-1]:
                lines.append(json.loads(line))
    
    with open("data/data.jsonl", "w") as f:
        for row in lines:
            f.write(json.dumps(row) + "\n")

def load_data():
    for k, v in datasets.items():
        print(f"create {k}")
        if os.path.exists(f"data/{k}.jsonl"):
            print(f"{k} exists")
            continue

        #cache_dir = "/p/alpha/hf_cache"
        if k == "wiki":
            d = load_dataset(v, language="en", date="20240601")
        elif k == "pol":
            d = load_dataset(v, "all")
        else:
            d = load_dataset(v)

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
    #load_data()
    combine_data()
