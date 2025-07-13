from ultralytics import YOLO
import cv2

# Carrega o modelo treinado
model = YOLO("runs/segment/yolov8_lixo5/weights/best.pt")

# Abre webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Faz inferência
    results = model.predict(source=frame, conf=0.3, show=True)

    # Pressione Q para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
