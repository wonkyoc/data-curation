from binidx import MMapIndexedDataset
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("RWKV/rwkv-4-world-7b", trust_remote_code=True)
#from tokenizer.rwkv_tokenizer import TRIE_TOKENIZER
#tokenizer = TRIE_TOKENIZER("/u/bfr4xr/git/RWKV-LM/RWKV-v5/tokenizer/rwkv_vocab_v20230424.txt")

input_file = "/bigtemp/bfr4xr/uncopyright_pile/pile"
#input_file = "/p/alpha/data"
CTX_LEN = 512

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

data = MMapIndexedDataset(input_file)
data_len = len(data)
data_size = len(data._bin_buffer) // data._index._dtype_size

TODO = [0, data_len - 1]
PREVIEW_LIMIT = 100
for idx in TODO:
    ptr, size = data._index[idx]
    dix = data.get(idx=idx, offset=0, length=size).astype(int)
    print("-" * 70 + f"[{input_file} idx {idx} sz {size}]")
    assert dix[-1] == 0
    dix = dix[:-1]
    if len(dix) > PREVIEW_LIMIT:
        try:
            print(tokenizer.decode(dix[:PREVIEW_LIMIT], skip_special_tokens=True))
        except:
            try:
                print(tokenizer.decode(dix[: PREVIEW_LIMIT + 1]))
            except:
                print(tokenizer.decode(dix[: PREVIEW_LIMIT + 2]))
        print("· " * 30)
        try:  # avoid utf-8 bug
            print(tokenizer.decode(dix[-PREVIEW_LIMIT:], skip_special_tokens=True))
        except:
            try:
                print(tokenizer.decode(dix[-PREVIEW_LIMIT - 1 :]))
            except:
                print(tokenizer.decode(dix[-PREVIEW_LIMIT - 2 :]))
    else:
        print(tokenizer.decode(dix))

print(f"{'-'*80}\n### Final {input_file}.bin/idx has {data_size} tokens, {data_len} items. Dtype {data._index.dtype}")

if data_size >= CTX_LEN * 3:
    n_chunk = int(data_size // CTX_LEN) - 1
    for i in range(n_chunk, 0, -1):
        if i % 3 == 2:
            if is_prime(i):
                print(f"\n### magic_prime = {i} (for ctxlen {CTX_LEN})\n")
                exit(0)
