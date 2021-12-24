
import json
from typing import List

from generator.forms import BonForm

from generator.models import Bon
import time
import os
import subprocess

def loadData():
    f = open('src/fixtures/MOCK_DATA.json')
    data = json.load(f)
    return data

def bonFromJson(item):
    bon = Bon()
    bon.id = item["id"]
    bon.date = item["date"]
    bon.autoNumerotation = item["autoNumerotation"]
    bon.nonReductibleCommand = item["nonReductibleCommand"]
    bon.editionDomTom = item["editionDomTom"]
    bon.socialReason = item["socialReason"]
    bon.representedBy = item["representedBy"]
    bon.adresse = item["adresse"]
    bon.adresseComplement = item["adresseComplement"]
    bon.postalCode = item["postalCode"]
    bon.city = item["city"]
    bon.phoneOrFax = item["phoneOrFax"]
    bon.portable = item["portable"]
    bon.email = item["email"]
    bon.website = item["website"] 
    bon.firstDeploy = item["firstDeploy"]
    bon.nbDeployOrdered = item["nbDeployOrdered"]
    bon.encart = item["encart"]
    bon.bdcLocality = item["bdcLocality"]
    bon.sector = item["sector"]
    bon.priceHT = item["priceHT"]
    bon.tva = 1.2
    bon.totalTTC = item["totalTTC"]
    bon.totalHT = item["totalHT"]
    bon.commercialContact = item["commercialContact"]
    bon.observations = item["observations"]
    return bon

def bonToJson(bon : Bon):
    item = {}
    item["id"] = bon.id  
    item["date"] = bon.date  
    item["autoNumerotation"] = bon.autoNumerotation  
    item["nonReductibleCommand"] = bon.nonReductibleCommand  
    item["editionDomTom"] = bon.editionDomTom  
    item["socialReason"] = bon.socialReason  
    item["representedBy"] = bon.representedBy  
    item["adresse"] = bon.adresse  
    item["adresseComplement"] = bon.adresseComplement  
    item["postalCode"] = bon.postalCode  
    item["city"] = bon.city  
    item["phoneOrFax"] = bon.phoneOrFax  
    item["portable"] = bon.portable  
    item["email"] = bon.email  
    item["website"] = bon.website   
    item["firstDeploy"] = bon.firstDeploy  
    item["nbDeployOrdered"] = bon.nbDeployOrdered   
    item["tva"] = bon.tva   
    item["encart"] = bon.encart  
    item["bdcLocality"] = bon.bdcLocality  
    item["sector"] = bon.sector  
    item["priceHT"] = bon.priceHT  
    item["totalTTC"] = bon.totalTTC
    item["totalHT"] = bon.totalHT
    item["commercialContact"] = bon.commercialContact
    item["observations"] = bon.observations
    return item

def loadFixtures() -> List[Bon]:
    result = []
    for item in loadData():
        result.append(bonFromJson(item))
    return result


import pdfkit

from django.template import Context, Template


def generatePDF(item : Bon , siteUrl = "http://localhost:8000"):
    templatePlace = os.path.join(os.path.dirname(__file__), 'templates/generator/generate_template.html')

    print("bbbbbb ",templatePlace)

    f = open(templatePlace)
    template = Template(f.read())
    html = template.render(Context({"bon" : item , "siteUrl" : siteUrl}))

    title = str(time.time()) + ".pdf"
    

    if 'DYNO' in os.environ:
        print ('loading wkhtmltopdf path on heroku')
        WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf-pack')], # Note we default to 'wkhtmltopdf' as the binary name
        stdout=subprocess.PIPE).communicate()[0].strip()

        config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)
        pdfkit.from_string(html, 'generator/static/generator/pdfs/'+title , configuration=config)

    else:
        print ('loading wkhtmltopdf path on localhost')
        # MYDIR = os.path.dirname(__file__)    
        # WKHTMLTOPDF_CMD = os.path.join(MYDIR + "/static/executables/bin/", "wkhtmltopdf.exe")
        pdfkit.from_string(html, 'generator/static/generator/pdfs/'+title)
    

    


    return title


