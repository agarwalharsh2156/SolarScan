from ultralytics import YOLO
import os
from config import settings
BASE_DIR = settings.BASE_DIR

MODEL_PATH = os.path.join(BASE_DIR, 'detections', 'best.pt')
model = YOLO(MODEL_PATH)

def run_yolo(image_path):
    results = model(image_path)

    solar_panel_count = 0
    empty_roof_count = 0
    detection_array = []

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            coords = box.xyxy[0].tolist() # [x1, y1, x2, y2]
            
            if cls_id == 0:
                empty_roof_count += 1
            elif cls_id == 1:
                solar_panel_count += 1
                
            detection_array.append({
                "class": cls_id,
                "confidence": conf,
                "box": coords
            })

    return {
        "empty_roof_count": empty_roof_count,
        "solar_panel_count": solar_panel_count,
        "bounding_boxes": detection_array
    }