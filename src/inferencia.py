from ultralytics import YOLO
import cv2
import os

# Caminho para imagens
IMAGE_PATH = "data/beachlitter/exemplo.jpg"
MODEL_PATH = "yolov8n-seg.pt"

# Carrega o modelo
model = YOLO(MODEL_PATH)

# Faz inferência
results = model.predict(source=IMAGE_PATH, conf=0.3, save=True)

print("Inferência concluída. Verifique a pasta 'runs/segment/predict'.")
