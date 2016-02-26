from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Animal

# Create your views here.
def index(request):
    return HttpResponse("You're looking at question {}.")

def listing(request, id):
	newest_animals = Animal.objects.order_by('pub_date')[:5]

def category(request, id):
	return HttpResponse("You're looking at question {}.")

def result(request, id):
	return HttpResponse("You're looking at question {}.")
