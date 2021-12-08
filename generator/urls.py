from django.urls import path
from .views import generate , generate_failed , generate_template


urlpatterns = [
    path('generate/failed/', generate_failed , name="generate_failed"),
    path('generate/template/', generate_template , name="generate_template"),
    path('generate/', generate , name="generate"),
]