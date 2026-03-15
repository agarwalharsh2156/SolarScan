import uuid
from django.db import models
from django.conf import settings

class Detections(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable = False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, related_name= 'detections', null = True)
    address = models.CharField(max_length= 500, blank = True, null = True)
    lat = models.DecimalField(max_digits = 9, decimal_places= 6)
    long = models.DecimalField(max_digits = 9, decimal_places= 6)
    zoom_level = models.IntegerField(default = 18)
    depth = models.IntegerField(default = 2)
    satellite_img = models.ImageField(upload_to='satellite_images/%Y/%m/%d/')
    targets = models.IntegerField(default = 0, help_text="Total number of potential customers.")
    solarPans = models.IntegerField(default = 0, help_text='Total number of solar panels detected.')
    detection_array = models.JSONField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Detections at {self.address}: Total Solar Panels -> {self.solarPans}, Potential Customers -> {self.targets}'
# Create your models here.
