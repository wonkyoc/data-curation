#!/bin/bash

mkdir owt2
pushd owt2
echo "download owt2..."
#wget https://huggingface.co/datasets/segyges/OpenWebText2/resolve/main/openwebtext2.jsonl.zst.tar
echo "unzip owt2..."
tar xvf openwebtext2.jsonl.zst.tar
rm openwevtext2.jsonl.zst.tar
echo "convert owt2..."
popd
python zsd2jsonl.py
