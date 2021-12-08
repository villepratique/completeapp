from django.urls import path
from .views import index ,contact , search


urlpatterns = [
    path('', index , name="index"),
    path('search', search , name="search"),
    path('contact', contact , name="contact"),
]