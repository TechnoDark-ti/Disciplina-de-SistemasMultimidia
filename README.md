# Detecção de Lixo com YOLOv8 - SISTEMA DE MULTIMÍDIA

## DESCRIÇÃO
Projeto para detectar lixo em áreas costeiras usando segmentação com YOLOv8, baseado no artigo científico "Detecção de Lixo em Áreas Costeiras: Uma Aplicação com R-CNNs da Família YOLO".

## DIRETÓRIO
O projeto está estruturado da seguinte forma:
~~~bash
projeto-yolo-lixo/
│
├── .gitignore
├── README.md
├── requirements.txt
├── setup.sh                 # Script para configurar ambiente
├── yolov7/
│   └── ...                  # Código YOLOv7 clonado e adaptado
├── yolov8/
│   └── ...                  # Código YOLOv8 (Ultralytics)
├── data/
│   └── beachlitter/         # Dataset (link ou estrutura)
├── notebooks/
│   └── exploracao.ipynb     # Análise exploratória
├── scr/
│   ├── inferencia.py        # Segmentação com YOLO
│   └── treino.py            # Treinamento com YOLOv7/v8

~~~
Para os ambiente virtual do python, recomenda-se que seja feito ates do src/ </br>
O .gitignore que está presente já ignore automaticamente os demais arquivos desnecessários para o versionamento

## DEPENDENCIAS
- Python 3.11
- torch 
- torchvision
- ultralytics
- opencv-python
- labelme

## CONSTRUIR

Primeiramente, baixe o projeto ou faça pelo CLI do terminal com o git clone em uma pasta adqueada:
~~~git
git clone https://github.com/TechnoDark-ti/Disciplina-de-SistemasMultimidia.git
~~~
Para construir o projeto, é necessãrio que rode o arquivo setup.sh para preparar o ambiente </br>
~~~bash
sh setup.sh
~~~
Por fim, rode o ambiente dentro da pasta:
~~~bash
python3.11 venv Disciplina-de-SistemasMultimidia/bin/activate
~~~

## LICENCE

Este repositório é distribuído sob a Licença GPL v.3. Consulte o arquivo LICENSE para obter detalhes.
