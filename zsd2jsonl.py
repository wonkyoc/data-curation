import zstandard as zst
import io
import json
import os
from tqdm import tqdm

PATH = "/bigtemp/bfr4xr/raw_pile"
files = os.listdir(PATH)

for f in tqdm(files):
    input_file = f"{PATH}/{f}"
    output_file = f"/bigtemp/bfr4xr/decompressed_pile/{f[:-4]}"
    print(f"decompress: {input_file} > {output_file}")
    with open(input_file, 'rb') as fh:
        dctx = zst.ZstdDecompressor(max_window_size=2147483648)
        stream_reader = dctx.stream_reader(fh)
        text_stream = io.TextIOWrapper(stream_reader, encoding='utf-8')
        with open(output_file, "w") as f:
            for line in text_stream:
                obj = json.loads(line)
                new_obj = {"text": obj["text"]}
                f.write(json.dumps(new_obj) + "\n")
print("done")
