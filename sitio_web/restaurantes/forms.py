from django import forms
from .models import restaurantes
from django.core.exceptions import ValidationError


def valida_codigo_postal(value):
  if value < 10000 or value > 99999:
    raise ValidationError('%s no parece ser un código postal' % value)

def valida_building(value):
  if value < 0:
    raise ValidationError('%s no parece ser un número de edificio' % value)

def valida_latitud(value):
  if value < -90 or value > 90:
    raise ValidationError('%s no parece ser un valor correcto de latitud' % value)

def valida_longitud(value):
  if value < -90 or value > 90:
    raise ValidationError('%s no parece ser un valor correcto de longitud' % value)

def valida_barrio(value):
    validos = restaurantes.distinct('borough')

    if value not in validos:
      raise ValidationError('%s no parece ser un barrio de Nueva York' % value)


def valida_cocina(value):
    validos = restaurantes.distinct('cuisine')

    if value not in validos:
      raise ValidationError('%s no parece ser un tipo de cocina válido' % value)

def valida_nombre_busqueda(value):
  validos = restaurantes.distinct('name')

  if value not in validos:
    raise ValidationError('%s no parece ser un nombre de restaurante existente' % value)

def valida_id_busqueda(value):
  validos = restaurantes.distinct('restaurant_id')

  if value not in validos:
    raise ValidationError('%s no parece ser id de restaurante existente' % value)




class RestauranteForm(forms.Form):
    name    = forms.CharField(label='Nombre', max_length=60, strip=True, 
                             widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Nombre del restaurante',
                                      }))

    cuisine = forms.CharField(label='Tipo', max_length=80, validators=[valida_cocina], 
                                widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Tipo de cocina',
                                      }))

    borough = forms.CharField(label='Barrio', max_length=60,validators=[valida_barrio], 
                             widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Nombre del barrio',
                                      }))


    zipcode = forms.IntegerField(label='Código Postal', 
                                validators=[valida_codigo_postal],widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Código postal',
                                      }))

    street = forms.CharField(label='Calle', 
                                widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Nombre de la calle',
                                      }))

    building = forms.IntegerField(label='Número de edificio', 
                                validators=[valida_building],widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Número de edificio',
                                      }))

    lat = forms.FloatField(label='Latitud',
                                validators=[valida_latitud],widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Valor de la latitud',
                                      }))

    lon = forms.FloatField(label='Longitud', 
                                validators=[valida_longitud],widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Valor de la longitud',
                                      }))

class NombreRestaurante(forms.Form):
  ide = forms.CharField(label='Id del restaurante', validators=[valida_id_busqueda],
                          widget=forms.TextInput(attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Introduzca el id del restaurante.',
                                      })) 


class ChangeRestauranteForm(forms.Form):
    name    = forms.CharField(label='Nombre', max_length=60, strip=True,
                             widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Nombre del restaurante',
                                      }))

    cuisine = forms.CharField(label='Tipo', max_length=80, validators=[valida_cocina], 
                                widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Tipo de cocina',
                                      }))

    borough = forms.CharField(label='Barrio', max_length=60,validators=[valida_barrio],
                             widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Nombre del barrio',
                                      }))


    zipcode = forms.IntegerField(label='Código Postal',
                                validators=[valida_codigo_postal],widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Código postal',
                                      }))

    street = forms.CharField(label='Calle',
                                widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Nombre de la calle',
                                      }))

    building = forms.IntegerField(label='Número de edificio', 
                                validators=[valida_building],widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Número de edificio',
                                      }))

    lat = forms.FloatField(label='Latitud', 
                                validators=[valida_latitud],widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Valor de la latitud',
                                      }))

    lon = forms.FloatField(label='Longitud', 
                                validators=[valida_longitud],widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'Valor de la longitud',
                                      }))
