from django.shortcuts import render, HttpResponse, redirect
from .models import restaurantes
import json
from django.http import JsonResponse
from .forms import RestauranteForm, NombreRestaurante, ChangeRestauranteForm
from django.contrib.auth.decorators import login_required
from bson import ObjectId

# Create your views here.
def index(request):
	context = {}
	return render(request, 'test.html', context)


@login_required
def database(request):
	resultado = restaurantes.find({"borough": "Manhattan"}).limit(10)

	context = {
		"rows" : list(resultado)
	}

	return render(request, 'test.html', context)


def animaciones(request):
	context = {
		"animaciones" : True
	}

	return render(request, 'test.html', context)

@login_required
def pagination(request):
	resultado = restaurantes.find({"borough": "Manhattan"}).limit(10)

	lista = []
	for var in resultado:
		lista.append({"name" : var["name"], "address" : var["address"]["street"], "cuisine" : var["cuisine"], "id": var["_id"]})

	context = {
		"data" : lista,
	}

	return render(request, 'test.html', context)

@login_required
def getlist(request):
	num = int(request.GET.get('pagina', ''))

	result = restaurantes.find({"borough": "Manhattan"}).skip(num*10).limit(10)

	lista = []
	for var in result:
		lista.append({"name" : var["name"], "address" : var["address"]["street"], "cuisine" : var["cuisine"], "id": str(var["_id"])})

	return JsonResponse(lista, safe = False)

@login_required
def nuevo_restaurante(request):
	form = RestauranteForm()

	if request.method == 'POST':
		form = RestauranteForm(request.POST)
		

		if form.is_valid():                   
			datos = form.cleaned_data	
			
			restaurantes.insert_one(
				{
					"address:": {
						"street": datos['street'],
						"zipcode": datos['zipcode'],
						"building": datos['building'],
						"coord": [datos["lon"], datos["lat"]]
					},

					"borough": datos['borough'],
					"cuisine": datos['cuisine'],
					"name": datos['name']
				})

			return redirect('/restaurantes')

	context = {
		'form': form,
	}

	return render(request, 'form.html', context)

@login_required
def change_restaurante(request, ide):
	object_ide = ObjectId(ide)
	restaurante_actual = restaurantes.find_one({'_id': object_ide}, projection = {'name': 1, 'cuisine':1, 'borough':1, 'address.zipcode':1, 'address.street':1, 'address.building':1, 'address.coord':1, '_id':1})

	myinitial = {
        'name': restaurante_actual['name'],
        'cuisine': restaurante_actual['cuisine'],
        'borough': restaurante_actual['borough'],
        'zipcode': restaurante_actual['address']['zipcode'],
        'street': restaurante_actual['address']['street'],
        'building': restaurante_actual['address']['building'],
        'lat': restaurante_actual['address']['coord'][1],
        'lon': restaurante_actual['address']['coord'][0]
	}

	form = ChangeRestauranteForm(initial = myinitial)

	if request.method == 'POST':
		form = ChangeRestauranteForm(request.POST, initial = myinitial)
		
		if form.is_valid():                   
			datos = form.cleaned_data	
			
			restaurantes.update({"_id":object_ide},
				{	
					"name": datos['name'],
					"address": {
						"street": datos['street'],
						"zipcode": datos['zipcode'],
						"building": datos['building'],
						"coord": [datos["lon"], datos["lat"]]
					},

					"borough": datos['borough'],
					"cuisine": datos['cuisine'],
				})

			return redirect('/restaurantes')

	context = {
		'form': form,
		'id': ide,
	}

	return render(request, 'form_change.html', context)

@login_required
def map(request):
	resultado = list(restaurantes.find({"borough": "Manhattan"},projection={'address.coord':1, '_id':0}).limit(100))

	longitudes = []
	latitudes = []

	resultado_new = []
	for r in resultado:
		resultado_new.append(r["address"]["coord"])

	context = {
		"coord":resultado_new,
	}

	return render(request, 'maps.html', context)

def stadistic(request):
	groupby = list(restaurantes.aggregate(
	   [
	     { '$group': { "_id": "$cuisine", "count": { '$sum': 1 } } },
	     {'$sort':{"count":-1}}
	   ]
	))

	lista = []
	for var in groupby:
		lista.append([var["_id"],var["count"]])


	context = {
		'lista': lista,
	}

	return render(request, 'estadisticas.html', context)

def ajax(request):
	context = {
		"ajax": True,
	}
	return render(request, 'test.html', context)




def stadistic_ajax1(request):
	groupby = list(restaurantes.aggregate(
	   [
	     { '$group': { "_id": "$cuisine", "count": { '$sum': 1 } } },
	     {'$sort':{"count":-1}}
	   ]
	))

	lista = []
	for var in groupby:
		lista.append([var["_id"],var["count"]])


	return JsonResponse(lista, safe = False)



def stadistic_ajax2(request):
	groupby = list(restaurantes.aggregate(
	   [
	     { '$group': { "_id": "$borough", "count": { '$sum': 1 } } },
	     {'$sort':{"count":-1}}
	   ]
	))

	lista = []
	for var in groupby:
		lista.append([var["_id"],var["count"]])


	return JsonResponse(lista, safe = False)




