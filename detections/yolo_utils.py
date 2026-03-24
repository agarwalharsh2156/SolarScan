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
        # Get image dimensions from the result
        img_height, img_width = r.orig_shape
        
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            coords = box.xyxy[0].tolist()  # [x1, y1, x2, y2] - absolute coordinates
            
            # Convert to normalized coordinates (0-1)
            x1, y1, x2, y2 = coords
            x = x1 / img_width
            y = y1 / img_height
            width = (x2 - x1) / img_width
            height = (y2 - y1) / img_height
            
            if cls_id == 0:
                empty_roof_count += 1
                box_type = 'target'
            elif cls_id == 1:
                solar_panel_count += 1
                box_type = 'solar_panel'
            else:
                box_type = 'unknown'
                
            detection_array.append({
                "type": box_type,
                "x": x,
                "y": y,
                "width": width,
                "height": height,
                "confidence": conf
            })

    return {
        "empty_roof_count": empty_roof_count,
        "solar_panel_count": solar_panel_count,
        "bounding_boxes": detection_array
    }