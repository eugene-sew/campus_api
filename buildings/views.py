from rest_framework import generics
from .models import Building
from .serializers import BuildingSerializer

# Create your views here.

class BuildingList(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class BuildingDetail(generics.RetrieveAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
