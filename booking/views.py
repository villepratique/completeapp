from django.http.response import HttpResponseRedirect
# Create your views here.
from django.http import Http404
from django.shortcuts import render
from booking.forms import ContactForm

from generator.forms import BonForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html' )

def search(request):
    return render(request, 'search.html' )

def contact(request):
    form = ContactForm()
    if request.method == "POST" or None:
        form = ContactForm(request.POST or None)
        if  form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(request, 'contact.html' , {"form" : form})