from django.shortcuts import render

def hola(request):
    return render(request,'hola.html',{})

def productos(request):
    return render(request,'productos.html',{})

def contenidoDinamico(request, name):
    context = {'name':name}
    return render(request, 'contenidoDinamico.html',context)
