from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=255 , verbose_name="Nom")
    lastname = models.CharField(max_length=255 , verbose_name="Prénom")
    email = models.EmailField(verbose_name="E-mail")
    phone = models.CharField(max_length=255 , verbose_name="Téléphone")
    message = models.TextField( verbose_name="Message" , blank=True,null=True)