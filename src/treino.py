from ultralytics import YOLO

# Caminho para o modelo base
BASE_MODEL = "yolov8n-seg.pt"

# Caminho para o diretório com dataset.yaml (detalha caminhos de imagens e número de classes)
DATASET_CONFIG = "data/beachlitter.yaml"

# Inicializa o modelo
model = YOLO(BASE_MODEL)

# Treinamento
model.train(
    data=DATASET_CONFIG,
    epochs=50,
    imgsz=640,
    batch=8,
    name="yolov8_lixo",
    task="segment"
)
