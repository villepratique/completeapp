from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'core/registration/login.html')


def register(request):
    return render(request, 'core/register.html')
