from django.http import HttpResponse, JsonResponse
from django.http.response import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from booking.forms import ContactForm

from django.contrib.auth.decorators import login_required


from .models import Entreprise

def index(request):
    return render(request, 'booking/index/index.html' )

def search(request):
    e = Entreprise.objects.all()
    if request.method == 'GET':
        qd = request.GET
        if (qd.get("what")):
            e = e.filter(job=qd["what"])
        if (qd.get("who")):
            e = e.filter(job=qd["who"])
        if (qd.get("paris")):
            e = e.filter(job=qd["paris"])

        print(e.values())

    
    return render(request, 'booking/search.html' , {"data" : e} )

def contact(request):
    form = ContactForm()
    if request.method == "POST" or None:
        form = ContactForm(request.POST or None)
        if  form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(request, 'booking/contact.html' , {"form" : form})


def cgu(request):
    return render(request, 'booking/cgu/index.html' )

def legalmentions(request):
    return render(request, 'booking/legalmentions/index.html' )


def allnews(request):
    return render(request, 'booking/allnews.html' )


def dataJson(request):
    e = Entreprise.objects.all()
    result = []
    for item in e.values():
        print(item)
        result.append({
            "title" : item["title"] , 
            "streetNumber" : item["streetNumber"], 
            "streetName" : item["streetName"], 
            "city" : item["city"], 
            "phoneNumber" : item["phoneNumber"], 
            "job" : item["job"], 
            })
    return JsonResponse(result , 
    safe=False)

# def securising(request , content ):
#     return HttpResponse("bwOgeyjOK6W8CDcHfyFo5qdVW_c6Aa97pVbbqL5IQrA.mCuXI1Ccc3w8CsS33OiEWCrfA1QMZxRImKkYJqaG4yk")


# /etc/letsencrypt/live/www.mavillepratique.fr/privkey.pem
