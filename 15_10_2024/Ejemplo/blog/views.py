from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
 
def blog(request):
    template = loader.get_template('blog.html')
    context = {}
    return HttpResponse(template.render(context, request))
