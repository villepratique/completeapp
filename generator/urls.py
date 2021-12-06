from django.urls import path
from .views import generate , generate_failed


urlpatterns = [
    path('generate/failed/', generate_failed , name="generate_failed"),
    path('generate/', generate , name="generate"),
]