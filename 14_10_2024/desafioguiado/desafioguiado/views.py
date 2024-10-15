from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def home(request):
    return render(request,'home.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(template.render(context, request))

