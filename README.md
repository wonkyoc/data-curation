# A script for data curation

# Preload

```
# Load dataset repo
git submodule init
git submodule update
```


# Guideline

Step 0: Use available data

Please use in our dept project `/p/alpha/{data.bin, data.idx, data.txt}`. 
Currently, `/p/alpha` is available for Prof. Lin, Wang, Choe.
The following steps require A LOT OF TIME to produce. The size of data is about 140GB and it contains web, wiki, and various.
`data.txt` contains a magic number.

```
cp /p/alpha/data.* {path}/RWKV-LM/RWKV-v5/data/
```

Step 1: collect dataset. 

There are two ways: (1) download it from huggingface.
This can be done by `load_dataset()`[[link](https://huggingface.co/docs/datasets/v2.20.0/loading)]
(2) download a raw file from a github repo or website. This should be manually done.

Step 2: convert datasets to the RWKV format. RWKV requires a specific dictionary format:

```
{"text": "content 1"}\n
{"text": "content 2"}\n
{"text": "content 3"}\n
```

Once a pile of data is converted to the format, save it as `.jsonl`. 
To achieve this, see and use `python collect_data.py`.

Step 2-1: zstandard -> jsonl. 

The data format is sometimes compressed as zstandard. Use `zsd2jsonl.py` to convert it to .jsonl

Step 3: combine datasets to a single file. 

If we have curated datasets then we
need to make a single big file. This can be done by `combine_data()` in `collect_data.py`

```
data/a.jsonl -->
data/b.jsonl -->    data/data.jsonl
data/c.jsonl -->
```

Step 4: convert .json to .binidx. 

The default data type of RWKV is `binidx`, which has two separated files: the binary data and its corresponding indices. 
Each GPU (or computing unit) starts from index 0 and based on the index, it generates a "random" index by multiple factors: # of epoch, rank, and the magic number. This random index is a starting index of input tokens. The trainer extracts a ctx_len (e.g., 512 or 4096) tokens from this index.

To conver .json, use `RWKV-LM/RWKV-v5/make_data.py`:

```
python make_data.py [filename] [num_suffle] [ctx_length]
python make_data.py data.jsonl 1 512 > data.txt
```
This takes ages if the size of datasets is huge. Once this operations done, it will print out a magic number.


# Rivanna

To access to the server, use the below cmd. A password is the general UVA paasword, NOT CS PW.

```
ssh [computing id]@login.hpc.virginia.edu
```


- `pretrain.slurm`: a file is for slurm on Rivanna.


# Dataset

- Openweb
    - [x] [OpenWebText2](https://openwebtext2.readthedocs.io/en/latest/)
- Wikipedia
    - [x] [Wikipedia/en/](https://huggingface.co/datasets/olm/wikipedia)
- Books
    - [x] [PG19](https://huggingface.co/datasets/deepmind/pg19)
- Academic
    - [ ] [PhilPapers](https://github.com/thoppe/The-Pile-PhilPapers?tab=readme-ov-file)
- Legal
    - [ ] [Pile of Law](https://huggingface.co/datasets/pile-of-law/pile-of-law)
- Social
    - [x] [Ubuntu IRC](https://github.com/EleutherAI/pile-ubuntu-irc)
- Various
    - [x] [Minipile](https://huggingface.co/datasets/JeanKaddour/minipile)
    - [x] [Dolly](https://huggingface.co/datasets/databricks/databricks-dolly-15k)
