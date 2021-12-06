from os import error
from django.http.response import HttpResponseRedirect
# Create your views here.
from django.http import Http404
from django.shortcuts import render

from generator.forms import BonForm

from generator.helper import generatePDF, loadData
from django.contrib.auth.decorators import login_required

@login_required
def generate(request):
    if request.method == 'POST':
        form = BonForm(request.POST)
        if form.is_valid():
            bon = form.save(commit=False)
            bon.owner = request.user
            bon.ownerName = request.user.username
            pdfId = generatePDF(bon)
            bon.filename = pdfId
            bon.save()
            try:
                pdfId = generatePDF(bon)
                return HttpResponseRedirect('/static/generator/pdfs/'+ pdfId)
            except error:
                print(error)
                return HttpResponseRedirect('/bdc/generate/failed/')
            
    else:
        data = loadData()
        item = data[0]
        form = BonForm(item)

    return render(request, 'template.html', {'form': form})


def generate_failed(request):
    return render(request, 'generate_failed.html')
