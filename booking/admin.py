from django.contrib import admin

# Register your models here.
from .models import Contact , Entreprise
admin.site.register(Contact)
admin.site.register(Entreprise)