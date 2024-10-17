from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

#def revisar(request,bodega):
 #   context = {'bodega':bodega}
 #   return render(request,'stock/revisar.html',context)

def revisar(request,bodega):
    template = loader.get_template('revisar.html')
    context = {'bodega':bodega}
    return HttpResponse(template.render(context, request))

