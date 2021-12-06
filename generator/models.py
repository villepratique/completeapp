from django.db import models

# Create your models here.
from django.db import models

class Bon(models.Model):
    CHOICES = (
        ("3", 3),
        ("6", 6),
        ("9", 9),
        ("12", 12),
    )

    owner = models.ForeignKey('core.User' , on_delete=models.SET_NULL , null=True)
    ownerName = models.CharField(max_length=255 , verbose_name="ownerName")
    filename = models.CharField(max_length=255 , verbose_name="Nom du fichier")

     

    # Informations entête
    date = models.DateField(max_length=30 , verbose_name="")
    autoNumerotation = models.BooleanField(default=False , verbose_name="Numérotation automatique")
    nonReductibleCommand = models.BooleanField(default=False , verbose_name="Commande non reconductible ")
    editionDomTom = models.BooleanField(default=False , verbose_name="Edition DOM/TOM ")
    # Informations client 
    socialReason = models.CharField(max_length=255 , verbose_name="Raison sociale")
    representedBy = models.CharField(max_length=255 , verbose_name="Représentée par")
    adresse = models.CharField(max_length=255 , verbose_name="Adresse")
    adresseComplement = models.CharField(max_length=255 , verbose_name="Complément d'adresse")
    postalCode = models.CharField(max_length=255 , verbose_name="Code postal")
    city = models.CharField(max_length=255 , verbose_name="Ville")
    phoneOrFax = models.CharField(max_length=255 , verbose_name="Téléphone / Fax")
    portable = models.CharField(max_length=255 , verbose_name="Portable")
    email = models.EmailField(verbose_name="Email (obligatoire)")
    website = models.URLField(verbose_name="Site web")
    # Mise en ligne
    firstDeploy = models.DateField(verbose_name="Première mise en ligne programmée le")
    nbDeployOrdered = models.CharField(max_length=255 , choices= CHOICES , verbose_name="Nombre de mise en ligne commandées" )
    # Bon de commande 
    encart = models.CharField(max_length=255 , verbose_name="Encart")
    bdcLocality = models.CharField(max_length=255 , verbose_name="Localité / Ville")
    sector = models.CharField(max_length=255 , verbose_name="Secteur d'activité")
    priceHT = models.DecimalField(decimal_places=2 , max_digits=19 , verbose_name="Montant H.T. (par mise en ligne)")
    tva = 19.80
    # tva = models.DecimalField(decimal_places=2)
    totalTTC = models.DecimalField(decimal_places=2 , max_digits=19 , verbose_name="Total T.T.C. (par mise en ligne)")
    totalHT = models.DecimalField(decimal_places=2 , max_digits=19 , verbose_name="Total H.T. (de la campagne)")
    commercialContact = models.CharField(max_length=255 , verbose_name="Contact commercial")
    observations = models.TextField(verbose_name="Observations")

    def __str__(self) -> str:
        return f"id {self.id} - {self.email}"

    