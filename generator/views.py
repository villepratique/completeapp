from os import error
from django.http.response import HttpResponseRedirect
# Create your views here.
from django.http import Http404
from django.shortcuts import render

from generator.forms import BonForm

from generator.helper import generatePDF, loadData, loadFixtures
from django.contrib.auth.decorators import login_required

@login_required
def generate(request):
    if request.method == 'POST':
        form = BonForm(request.POST)
        
        if form.is_valid():
            bon = form.save(commit=False)
            bon.owner = request.user
            bon.ownerName = request.user.username
            bon.save()
            pdfId = generatePDF(bon)
            bon.filename = pdfId
            return HttpResponseRedirect('/static/generator/pdfs/'+ pdfId)

            # try:
            #     bon.save()
            #     pdfId = generatePDF(bon)
            #     bon.filename = pdfId
                
            #     return HttpResponseRedirect('/static/generator/pdfs/'+ pdfId)
            # except error:
            #     print(error)
            #     return HttpResponseRedirect('/bdc/generate/failed/')  
    else:
        data = loadData()
        item = data[0]
        form = BonForm(item)

    return render(request, 'generator/template.html', {'form': form})


def generate_failed(request):
    return render(request, 'generator/generate_failed.html')


def generate_template(request):
    data = loadFixtures()
    bon = data[0]
    return render(request, 'generator/generate_template.html' , {"bon" : bon})
