from datasets import load_dataset
import json
import os.path

datasets = {
        #"dolly": "databricks/databricks-dolly-15k"  # works
        #"minipile": "JeanKaddour/minipile",     # works
        "wiki": "olm/wikipedia",               # works but huge
        #"pg19": "deepmind/pg19",               # works 
        #"owt2": None,                          # works
        #"irc": None,                           # works
        #"philpaper: None,                      # WIP from git repo
        #"pol": "pile-of-law/pile-of-law",      # works
        }



def combine_data():
    lines = []

    if os.path.exists("data/data.jsonl"):
        assert(f"{k}.jsonl exist. Please delete the file")

    for k, v in datasets.items():
        filename = f"data/{k}.jsonl"

        if os.path.exists(filename) == False:
            assert(f"{k}.jsonl not exist")

        with open(filename, "r") as f:
            chunk = f.read().split("\n")
            for line in chunk[:-1]: # the last line is empty
                lines.append(json.loads(line))
    
    with open("data/data.jsonl", "w") as f:
        for row in lines:
            f.write(json.dumps(row) + "\n")

def load_data():
    for k, v in datasets.items():
        if os.path.exists(f"data/{k}.jsonl"):
            print(f"{k} exists")
            continue

        print(f"create {k}")

        #cache_dir = "/p/alpha/hf_cache"
        if k == "wiki":
            d = load_dataset("wikimedia/wikipedia", "20231101.en")
        elif k == "pol":
            d = load_dataset(v, "all")
        elif k == "irc":
            assert("use submodule repo: pile-ubuntu-irc")
        elif  k == "owt2":
            assert("use wget: bash download.sh")
        else:
            d = load_dataset(v)

        texts = []
        for row in d["train"]:
            text = ""
            for key, value in row.items():
                text += f"{key}: {value}"
            texts.append({"text": text})
        
        # write concat jsonl
        with open(f"data/{k}.jsonl", "w") as f:
            for row in texts:
                f.write(json.dumps(row) + "\n")

if __name__ == "__main__":
    load_data()
    #combine_data()
