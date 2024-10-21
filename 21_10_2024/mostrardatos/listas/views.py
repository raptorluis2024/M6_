from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
 
def mostrar_lista(request):
    template = loader.get_template('mostrar_lista.html')
    cursos = ["Python", "Django","Fundamentos del desarrollo web",
"Bases de datos SQL"]
    #cursos = None
    context = {"cursos":cursos}
    return HttpResponse(template.render(context, request))
