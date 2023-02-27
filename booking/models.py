from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=255 , verbose_name="Nom")
    lastname = models.CharField(max_length=255 , verbose_name="Prénom")
    email = models.EmailField(verbose_name="E-mail")
    phone = models.CharField(max_length=255 , verbose_name="Téléphone")
    message = models.TextField( verbose_name="Message" , blank=True,null=True)


class Entreprise(models.Model):
    title = models.CharField(max_length=255 , verbose_name="Titre",unique=True)
    streetNumber = models.CharField(max_length=255 , verbose_name="Numéro de rue")
    streetName = models.CharField(max_length=255 , verbose_name="Nom de la rue")
    city = models.CharField(max_length=255 , verbose_name="Ville")

    phoneNumber = models.CharField(max_length=255 , verbose_name="numéro de téléphone")
    job = models.CharField(max_length=255 , verbose_name="Job")
    photo = models.ImageField(upload_to='soc_photos' , blank=True,null=True)
    photoLink = models.CharField(max_length=255 , verbose_name="Lien de la photo",null=True,blank=True)


    def __str__(self) -> str:
        return f"{self.id}-{self.title} - {self.job}"