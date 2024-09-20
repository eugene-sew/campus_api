from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField(null=True, blank=True)  # Added latitude field
    longitude = models.FloatField(null=True, blank=True)  # Added longitude field

    def __str__(self):
        return self.name

class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='places/')
