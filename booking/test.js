// Obtenir le top des activités

var result =[]
document.querySelectorAll(".list-activity").forEach(function(e) {
    title = e.textContent.trim();
    result.push(title)
    })
print(result)


var topActivites = [
    "Restaurants",
    "Coiffeurs",
    "Clubs de sport divers",
    "Agences immobilières",
    "Boulangeries-pâtisseries (artisans)",
    "Garages automobiles",
    "Clubs d'athlétisme",
    "Dentistes",
    "Instituts de beauté",
    "Infirmiers (cabinets, soins à domicile)",
    "Taxis",
    "Fleuristes",
    "Plombiers",
    "Bureaux de tabacs",
    "Medecins medecine generale",
    "Auto-écoles",
    "Pharmacies",
    "Pompes funèbres",
    "Courrier colis envoi distribution",
    "Transport de colis",
    "Livraison de colis",
    "Emploi travail services publics",
    "Transport ferroviaire",
    "Supermarché",
    "Supermarchés hypermarchés",
    "Hypermarché",
    "Caisse allocations familiales",
    "Sécurité sociale",
    "Ophtalmologiste",
    "Trésorerie public",
    "Trésor public",
    "Enseignement supérieur public",
    "Mutuelles",
    "Dentistes chirurgiens dentistes et docteurs en chirurgie dentaire",
    "Agence de voyage",
    "Mairie",
    "Kinésithérapeute",
    "Magasin de sport",
    "Associations culturelles éducatives de loisirs",
    "Cliniques",
    "Dermatologue",
    "Association culturelle",
    "Cinéma",
    "Vêtements hommes",
    "Accès internet",
    "Fournisseurs d'accès internet",
    "Chaussures",
    "Salle de concert",
    "Salle de spectacle",
    "Salles de jeux en réseaux",
    "Sous-préfecture",
    "Gendarmerie nationale",
    "Services de gendarmerie de police",
    "Sport stades et complexes sportifs",
    "Foire exposition",
    "Parking",
    "Crédit a la consommation établissements",
    "Grand magasin",
    "Hlm",
    "Bureaux de tabac",
    "Librairie",
    "Laboratoires d'analyses de biologie médicale",
    "Vêtements enfants",
    "Bar à thèmes",
    "Bars bars a thèmes",
    "Parfumerie",
    "Garage automobile",
    "Garages automobiles",
    "Location appartement",
    "Caisses de retraite",
    "Caisses de retraite et de prévoyance",
    "Centre radiologie",
    "Imagerie médicale",
    "Cabinet de radiologie",
    "Centre d'imagerie médicale",
    "Discount destockage dégriffés",
    "Matériel informatique",
    "Vente de consommables et de matériel informatique",
    "Vente de matériel de consommables d'informatique",
    "Docteur orl",
    "Médecins orl",
    "Médecin orl",
    "Vétérinaire",
    "Transport touristique en autocars",
    "Station service",
    "Magasin de meubles",
    "Magasins de meubles",
    "Mutuelles d'assurances",
    "Pâtisserie",
    "Podologue",
    "Boucherie",
    "Transport aérien",
    "Orthodontiste",
    "Bijouterie fantaisie",
    "Rhumatologue",
    "Consulat",
    "Ambassade",
    "Ambassades consulats"
  ]
let villes = ["Paris", "Marseille", "Lyon", "Toulouse", 
"Nice", "Nantes", "Strasbourg", "Montpellier", "Bordeaux", "Lille",
//  "Rennes", "Reims", "Le Havre", "Saint-Etienne", "Toulon", "Grenoble", "Dijon", "Angers", "Nîmes", "Villeurbanne"
];


  //

  var getRoadNumber = function(address){
    const regex = /^(\d+)\s/;
    const match = address.match(regex);
    const numero = match ? match[1] : null;
    return numero;
  }

  var JOB = "restaurants"
  var CITY = "Lille"

  function getOneInfo(infoElement,job,city){
    console.log(infoElement)
    let title = infoElement.querySelector("h3").textContent
    let address = infoElement.querySelector(".bi-address.small").textContent.trim().replace("\nVoir le plan","")
    let roadNb = getRoadNumber(address)
    let roadName = address.replace(`${roadNb} `,"")
    let img = infoElement.querySelector("figure")?.querySelector("img")?.src
    if(!img){
        img = ""
    }
    let phone =""
    let testphone =  infoElement.querySelector(".annonceur")
    if(testphone){
        phone = testphone.textContent.trim()
    }

    if(!phone){
       phone = infoElement.querySelector(".number-contact")?.textContent.replace(" Tél : ","")
    }


    let obj = {
        title,
        streetNumber : roadNb ,
        streetName : roadName,
        phoneNumber : phone,
        photo : img,
        job,
        city,
    }

    return obj
  }

  function getAllEnterprises(ville,jobRecherche){
    let result = []
    var all =  document.querySelectorAll('.bi.bi-generic') 
    all.forEach(function(el,index){
        result.push(getOneInfo(el,jobRecherche,ville))
    })
    console.log(result)
  }

  getAllEnterprises(CITY,JOB)


