from django.shortcuts import render,redirect,loader
from django.http import HttpResponse

def home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))

