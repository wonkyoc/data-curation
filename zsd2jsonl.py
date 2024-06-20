import zstandard as zst
import io
import json
import os

files =  os.listdir("owt2")

output_file = "data/owt2.json"

for f in files:
    input_file = f"owt2/{f}"
    print(input_file)
    with open(input_file, 'rb') as fh:
        dctx = zst.ZstdDecompressor(max_window_size=2147483648)
        stream_reader = dctx.stream_reader(fh)
        text_stream = io.TextIOWrapper(stream_reader, encoding='utf-8')
        with open(output_file, "a") as f:
            for line in text_stream:
                obj = json.loads(line)
                new_obj = {"text": obj["text"]}
                f.write(json.dumps(new_obj) + "\n")
