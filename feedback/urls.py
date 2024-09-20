from django.urls import path
from .views import feedback_list_create

urlpatterns = [
    path('feedback/', feedback_list_create, name='feedback-list-create'),
]
