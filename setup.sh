#!/bin/bash

brew install python@3.11 virtualenv

pip3 install -r requeriments.txt
pip3 install labelme

mkdir -p data/beachlitter/images/train
mkdir -p data/beachlitter/images/val
mkdir -p data/beachlitter/labels/train
mkdir -p data/beachlitter/labels/val
mkdir -p runs/

echo "path: data/beachlitter / train: images/train / val: images/val /  nc: 1 / names: ["lixo artificial"]/" > data/beachlitter.yaml
