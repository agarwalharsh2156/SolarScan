# detections/views.py
import json
import requests
import os
from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from .models import Detections
from .yolo_utils import run_yolo


@login_required
def map_interface(request):
    return render(request, 'detections/map.html')

@login_required
def process_map_click(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            lat = data.get('lat')
            lng = data.get('lng')
            zoom = data.get('zoom_level', 19)
            depth = data.get('depth', 2)
            address = data.get('address', '')

            if not lat or not lng:
                return JsonResponse({'error': 'Missing coordinates'}, status=400)

            # 1. Fetch satellite image securely via backend
            api_key = os.getenv("MAPS_API_KEY")
            img_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom={zoom}&size=640x640&maptype=satellite&scale={depth}&key={api_key}"
            img_response = requests.get(img_url)

            if img_response.status_code != 200:
                return JsonResponse({'error': 'Failed to fetch map image'}, status=502)

            # 2. Initialize database record mapping to your schema
            detection = Detections(
                user=request.user,
                address=address,
                lat=lat,
                long=lng,
                zoom_level=zoom,
                depth=depth
            )
            
            # 3. Save binary image directly to ImageField
            file_name = f"scan_{lat}_{lng}.jpg"
            detection.satellite_img.save(file_name, ContentFile(img_response.content), save=False)

            # 4. YOLO PLACEHOLDER
            # Once your custom model is trained to detect empty roofs and solar panels,
            # pass detection.satellite_img.path to the inference script here:
            # 
            results = run_yolo(detection.satellite_img.path)
            detection.targets = results.get('empty_roof_count', 0)
            detection.solarPans = results.get('solar_panel_count', 0)
            detection.detection_array = results.get('bounding_boxes', [])
            
            detection.save()

            return JsonResponse({
                'status': 'success',
                'targets': detection.targets,
                'solarPans': detection.solarPans,
                'bounding_boxes': detection.detection_array,
                'image_url': detection.satellite_img.url
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)