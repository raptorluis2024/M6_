from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def contenido(request):
    template = loader.get_template('contenido.html')
    lista = ['Andres','Juan','Ana','Patricia','Arnaldo']
    context = {'empleados':lista}
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def herencia1(request):
    template = loader.get_template('herencia1.html')
    context = {}
    return HttpResponse(template.render(context, request))