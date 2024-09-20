from django.shortcuts import render
from rest_framework import generics
from .models import Place
from .serializers import PlaceSerializer

# Create your views here.

class PlaceList(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceDetail(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
