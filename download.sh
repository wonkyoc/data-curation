#!/bin/bash

echo "download owt2..."
wget https://huggingface.co/datasets/segyges/OpenWebText2/resolve/main/openwebtext2.jsonl.zst.tar
echo "unzip owt2..."
tar xvf openwebtext2.jsonl.zst
echo "convert owt2..."
python zsd2jsonl.py
