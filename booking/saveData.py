from .models import Entreprise

import json
  
def saveData():
    # Opening JSON file
    f = open('booking/allrestaurants.json')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    for obj in data:
        title = obj["title"]
        print(title)
        existingSociety = Entreprise.objects.filter(title=title).first()
        print(existingSociety)
        if(existingSociety != None):
            continue

        streetNumber = obj["streetNumber"]
        if streetNumber == None:
            streetNumber = "N/A"
        society = Entreprise(
            title=title,
            streetNumber=streetNumber,
            streetName=obj["streetName"],
            city=obj["city"],
            phoneNumber=obj["phoneNumber"],
            job=obj["job"],photoLink=obj["photo"]
            )
        Entreprise.save(society)
    
    # Closing file
    f.close()



def removeAll():
    Entreprise.objects.all().delete()
#from booking.saveData import saveData,removeAll