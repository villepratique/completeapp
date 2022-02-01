from django.http import HttpResponse, JsonResponse
from django.http.response import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from booking.forms import ContactForm

from django.contrib.auth.decorators import login_required


from .models import Entreprise

def index(request):
    return render(request, 'booking/index/index.html' )

def sanitize(value : str):
    return value.strip().lower()

def search(request):
    e = Entreprise.objects.all()
    # print(e.values())
    if request.method == 'GET':
        qd = request.GET
        what , who , where = qd.get("what") , qd.get("who") , qd.get("where")

        what = sanitize(what)
        who = sanitize(who)
        where = sanitize(where)

        e = e.filter(city__icontains=where , job__icontains=what , title__icontains=who)

        # print(what , " " ,  who , " " ,  where)

        # if (what):
        #     print("what " , what)
        #     what = sanitize(what)
        #     e = e.filter(job__icontains=what)
        # if (who):
        #     print("who " , who)
        #     who = sanitize(who)
        #     e = e.filter(title__icontains=who)
        # if (where):
        #     print("where " , where)
        #     where = sanitize(where)
        #     print(e)
        #     e = e.filter(city__icontains=where)
        #     print(e)

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
