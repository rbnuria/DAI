# restaurantes/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^database/$', views.database, name='database'),
  url(r'^animaciones/$', views.animaciones, name='animaciones'),
  url(r'^pagination/$', views.pagination, name='pagination'),
  url(r'^getlist/$', views.getlist, name='getlist'),
  url(r'^nuevo_restaurante/$', views.nuevo_restaurante, name='nuevo_restaurante'),
  url(r'^map/$', views.map, name='map'),
  url(r'^stadistic/$', views.stadistic, name='stadistic'),
  url(r'^ajax/$', views.ajax, name='ajax'),
  url(r'^stadistic_ajax1/$', views.stadistic_ajax1, name='stadistic_ajax1'),
  url(r'^stadistic_ajax2/$', views.stadistic_ajax2, name='stadistic_ajax2'),
  url(r'^change_restaurante/(.*)/$', views.change_restaurante, name='change_restaurante'),
]