#!/bin/bash

cat <<EOF
 ____  _____ _____ _   _ ____  ____  _   _ 
/ ___|| ____|_   _| | | |  _ \/ ___|| | | |
\___ \|  _|   | | | | | | |_) \___ \| |_| |
 ___) | |___  | | | |_| |  __/ ___) |  _  |
|____/|_____| |_|  \___/|_| (_)____/|_| |_|
                                           
EOF

echo "Iniciando a configuração do ambiente Yolo Lixo Costeiro... Aguarde!"

OS_TYPE="$(uname-s)"

if ["$OS_TYPE" == "Darwin"]';then
   echo"Sistema Detectado: macOS"
   brew install python@3.11
elif ["OS_TYPE" == ""Linux"]; then
   sudo apt update
   sudo apt install python3.11 python3.11-virtualenv -y
else
   echo"Sistema não suportado! $OS_TYPE"
   exite 1
fi

python3.11 -m venv Disciplina-de-SistemasMultimidia
source Disciplina-de-SistemasMultimidia/bin/activate


pip3 install --upgrade pip
pip3 install -r requeriments.txt
pip3 install labelme


mkdir -p data/beachlitter/images/train
mkdir -p data/beachlitter/images/val
mkdir -p data/beachlitter/labels/train
mkdir -p data/beachlitter/labels/val
mkdir -p runs/


cat <<EOF > data/beachlitter.yaml
path: data/beachlitter
train: images/train
val: images/val
nc: 1
names: ["lixo artificial"]
EOF


echo "Setup finalizado com sucesso!"
echo "Ative o ambiente com: source bin/activate"
