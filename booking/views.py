from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from booking.forms import ContactForm

from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'booking/index/index.html' )

def search(request):
    return render(request, 'booking/search.html' )

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


def securising(request , content ):
    return HttpResponse("xxxxxxxxxxxx-yyyy.zzzzzzzzzzzzzzzzzzz")


