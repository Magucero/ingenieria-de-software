from django.http import HttpResponse
from django.shortcuts import render

contexto = {"nombre":"juancito",
            "esMayor":True,
            "mascotas": ["firu","boby", "michigan"]
                }
# Create your views here.
def saludo(request):
    return render(request,'saludo/index.html',contexto)
#nota establecer una ruta

def despedir(request):
    return render(request,"saludo/despedir.html",contexto)

def inicio(request):
    return HttpResponse("<h1> estoy en root</h1>")


#nuevo proyecto

