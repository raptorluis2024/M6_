from django.shortcuts import render

def about(request):
    return render(request,'about.html',{})

def home(request):
    return render(request,'home.html',{})

def listado(request):
    return render(request,'listado.html',{})

def contenidodinamico(request):
    animales = ['perro','gato','conejo','liebre']
    context = {'animales': animales}
    return render(request, 'contenidodinamico.html',context)
