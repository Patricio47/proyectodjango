from contextvars import Context
from django.http import HttpResponse
import random

from django.template import Template, Context, loader

def inicio(request):
    return HttpResponse("hola soy la nueva paginaXD")

def otra_vista(request):
    return HttpResponse("<h1>Este es un titulo en h1</h1>")

def numero_random (request):
    numero = random.randrange(15,180)
    texto= f"<h1> Este es tu numero random: {numero}</h1>"
    return HttpResponse(texto)


def numero_del_usuario (request, numero):
    texto= f"<h1> Este es tu numero: {numero}</h1>"
    return HttpResponse(texto)

def mi_plantilla(request):
    # plantilla = open(r"C:\Users\byawe\OneDrive\Escritorio\ProyectoDjango\proyectodjango\planitllas\mi_plantilla.html")
    template = loader.get_template("mi_plantilla.html")

    nombre = "Jorge"
    apellido = "Atahualpa"

    lista = [1,2,3,4,5,6]

    diccionario_de_datos = {
        "nombre" : nombre, 
        "apellido" : apellido,
        "nombre_largo": len(nombre), 
        "lista": lista
    }
    # template = Template(plantilla.read())

    # context = Context(diccionario_de_datos)

    plantilla_preparada = template.render(diccionario_de_datos)
    
    return HttpResponse(plantilla_preparada)