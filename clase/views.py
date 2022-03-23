from django.http import HttpResponse
from django.shortcuts import render
from clase.models import Curso
import random

def nuevo_curso(request):
    camada = random.randrange(1500, 3000)
    nuevo_curso = Curso(nombre="Curso Python", camada=camada)
    nuevo_curso.save()
    return HttpResponse(f"Se creo el curso {nuevo_curso.nombre} camada{camada}")
