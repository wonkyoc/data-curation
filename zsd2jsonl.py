import zstandard as zst
import io
import json

file = "/p/alpha/data-curation/pile-ubuntu-irc/out/data_0_time1718752937_default.jsonl.zst"

with open(file, 'rb') as fh:
    dctx = zst.ZstdDecompressor(max_window_size=2147483648)
    stream_reader = dctx.stream_reader(fh)
    text_stream = io.TextIOWrapper(stream_reader, encoding='utf-8')
    with open("data/irc.jsonl", "w") as f:
        for line in text_stream:
            obj = json.loads(line)
            new_obj = {"text": obj["text"]}
            f.write(json.dumps(new_obj) + "\n")



