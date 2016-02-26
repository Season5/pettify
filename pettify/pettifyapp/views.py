from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Animal

# Create your views here.
def index(request):
    return render(request, 'pettifyapp/index.html')

def listing(request):
	newest_animals_list = Animal.objects.order_by('category')
	# order_by('pub_date')[:5]
	template = loader.get_template('pettifyapp/animals.html')
	context = {
		'newest_animals_list': newest_animals_list
	}
	return render(request, 'pettifyapp/animals.html', context)

def category(request):
	return render(request, 'pettifyapp/category.html')

def result(request, id):
	animal = get_object_or_404(Animal, pk=id)
	return render(request, 'pettifyapp/one.html', {'animal': animal})
