from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render

from .forms import NewUserForm
from django.contrib.auth import login, logout
from django.contrib import messages

def register(request):
	form = NewUserForm()

	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			# messages.success(request, "Registration successful." )
			return redirect("home")
		# messages.error(request, "Unsuccessful registration. Invalid information.")
	
	return render (request,'registration/register.html', {"form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

 