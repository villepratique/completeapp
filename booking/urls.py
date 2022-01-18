from django.urls import path
from .views import index ,contact , search , cgu , legalmentions 


urlpatterns = [
    path('', index , name="home"),
    path('search', search , name="search"),
    # path('news', news , name="news"),
    path('contact', contact , name="contact"),
    path('conditions-generales', cgu , name="cgu"),
    path('mentions-legales', legalmentions , name="legalmentions"),

    # path('.well-known/acme-challenge/<str:content>', securising , name="securising"),
]


