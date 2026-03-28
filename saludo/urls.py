
#en este archivo vamos a enlazar los endpoints con cada una de las vistas que cada uno de notros tengamos

from django.urls import path,include

from . import views

#va a tener una variable que sivre de cenral 
urlpatterns=[
    path('saludar/', views.saludo, name="saludo"),
    path('despedir/', views.despedir, name="despedir"),
    path('', views.inicio, name="inicio")


]