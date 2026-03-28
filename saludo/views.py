from django.http import HttpResponse


# Create your views here.
def saludo(request):
    return HttpResponse("<h1> Hola mundor</h1>")


#nota establecer una ruta

def despedir(request):
    return HttpResponse("<h1> chau mundor</h1>")

def inicio(request):
    return HttpResponse("<h1> estoy en root</h1>")