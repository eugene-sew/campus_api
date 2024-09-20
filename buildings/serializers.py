from rest_framework import serializers
from .models import Building, BuildingImage, Office, LectureHall

class BuildingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingImage
        fields = ['image']

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ['name', 'floor']

class LectureHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureHall
        fields = ['name', 'floor', 'capacity']

class BuildingSerializer(serializers.ModelSerializer):
    images = BuildingImageSerializer(many=True, read_only=True)

    class Meta:
        model = Building
        fields = ['id', 'name', 'description', 'floors', 'latitude', 'longitude', 'images', 'offices', 'lecture_halls']
