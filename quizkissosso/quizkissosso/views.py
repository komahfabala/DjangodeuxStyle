from django.shortcuts import render 
from . import views

#la page d'accueil pour le site
def home(request):
	return render(request ,'pages/home.html') 

#la page a propos
def about(request) :
	return render(request,'about.html')

#la page pour contacte le resposable du site 
def contact(request):
	return render(request,'contact.html')