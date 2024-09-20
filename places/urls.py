from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import PlaceList, PlaceDetail

urlpatterns = [
    path('places/', PlaceList.as_view(), name='place-list'),
    path('places/<int:pk>/', PlaceDetail.as_view(), name='place-detail'),
]
