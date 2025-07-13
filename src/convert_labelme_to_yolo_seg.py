import os
import json

# Caminhos
LABELME_DIR = 'data/beachlitter/annotations'
YOLO_LABELS_DIR = 'data/beachlitter/labels/train'
IMAGE_DIR = 'data/beachlitter/images/train'

os.makedirs(YOLO_LABELS_DIR, exist_ok=True)

for filename in os.listdir(LABELME_DIR):
    if filename.endswith('.json'):
        json_path = os.path.join(LABELME_DIR, filename)
        with open(json_path, 'r') as f:
            data = json.load(f)

        img_width = data['imageWidth']
        img_height = data['imageHeight']

        label_name = os.path.splitext(filename)[0]
        output_path = os.path.join(YOLO_LABELS_DIR, label_name + '.txt')

        with open(output_path, 'w') as out_file:
            for shape in data['shapes']:
                if shape['shape_type'] != 'polygon':
                    continue
                points = shape['points']
                line = '0'  # classe lixo artificial
                for x, y in points:
                    x_norm = x / img_width
                    y_norm = y / img_height
                    line += f' {x_norm:.6f} {y_norm:.6f}'
                out_file.write(line + '\n')

print("Conversão concluída!")
