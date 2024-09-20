from django.db import models

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    floors = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class BuildingImage(models.Model):
    building = models.ForeignKey(Building, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='buildings/')

class Office(models.Model):
    building = models.ForeignKey(Building, related_name='offices', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    floor = models.PositiveIntegerField()

class LectureHall(models.Model):
    building = models.ForeignKey(Building, related_name='lecture_halls', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    floor = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
