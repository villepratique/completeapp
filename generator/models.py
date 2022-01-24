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
    date = models.DateField(max_length=30 , verbose_name="Date" , blank=True , null=True)
    autoNumerotation = models.BooleanField(default=False , verbose_name="Numérotation automatique" , blank=True , null=True)
    nonReductibleCommand = models.BooleanField(default=False , verbose_name="Commande non reconductible " , blank=True , null=True)
    editionDomTom = models.BooleanField(default=False , verbose_name="Edition DOM/TOM " , blank=True , null=True)
    # Informations client 
    socialReason = models.CharField(max_length=255 , verbose_name="Raison sociale" , blank=True , null=True)
    representedBy = models.CharField(max_length=255 , verbose_name="Représentée par" , blank=True , null=True)
    adresse = models.CharField(max_length=255 , verbose_name="Adresse" , blank=True , null=True)
    adresseComplement = models.CharField(max_length=255 , verbose_name="Complément d'adresse" , blank=True , null=True)
    postalCode = models.CharField(max_length=255 , verbose_name="Code postal" , blank=True , null=True)
    city = models.CharField(max_length=255 , verbose_name="Ville" , blank=True , null=True)
    phoneOrFax = models.CharField(max_length=255 , verbose_name="Téléphone / Fax" , blank=True , null=True)
    portable = models.CharField(max_length=255 , verbose_name="Portable" , blank=True , null=True)
    email = models.EmailField(verbose_name="Email (obligatoire)" , blank=True , null=True)
    website = models.URLField(verbose_name="Site web" , blank=True , null=True)
    # Mise en ligne
    # firstDeploy = models.DateField(verbose_name="Première mise en ligne programmée le" , blank=True , null=True)
    firstDeploy = models.CharField(max_length=255 , verbose_name="Première mise en ligne programmée le" , blank=True , null=True)

    nbDeployOrdered = models.CharField(max_length=255 , choices= CHOICES , verbose_name="Nombre de mise en ligne commandées" , blank=True , null=True )
    # Bon de commande 
    encart = models.CharField(max_length=255 , verbose_name="Encart" , blank=True , null=True)
    bdcLocality = models.CharField(max_length=255 , verbose_name="Localité / Ville" , blank=True , null=True)
    sector = models.CharField(max_length=255 , verbose_name="Secteur d'activité" , blank=True , null=True)
    priceHT = models.DecimalField(decimal_places=2 , max_digits=15 , verbose_name="Montant H.T. (par mise en ligne)" , blank=True , null=True)
    tva = models.DecimalField(decimal_places=2 , max_digits=15 , verbose_name="Tva" , blank=True , null=True)
    # tva = models.DecimalField(decimal_places=2)
    totalTTC = models.DecimalField(decimal_places=2 , max_digits=15 , verbose_name="Total T.T.C. (par mise en ligne)" , blank=True , null=True)
    totalHT = models.DecimalField(decimal_places=2 , max_digits=15 , verbose_name="Total H.T. (de la campagne)" , blank=True , null=True)
    commercialContact = models.CharField(max_length=255 , verbose_name="Contact commercial" , blank=True , null=True)
    observations = models.TextField(verbose_name="Observations" , blank=True , null=True)

    def __str__(self) -> str:
        return f"Bon N°{self.id} - créé par {self.ownerName}"



