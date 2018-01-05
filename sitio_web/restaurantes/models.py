from django.db import models

# Create your models here.

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test					#base de dato
restaurantes = db.restaurants		#colección