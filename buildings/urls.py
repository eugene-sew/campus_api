from django.urls import path
from .views import BuildingList, BuildingDetail

urlpatterns = [
    path('buildings/', BuildingList.as_view(), name='building-list'),
    path('buildings/<int:pk>/', BuildingDetail.as_view(), name='building-detail'),
]
