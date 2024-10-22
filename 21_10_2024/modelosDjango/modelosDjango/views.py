from django.shortcuts import render,redirect
from articleManagement.models import Article

from articleManagement.forms import FormularioArticle

# Create your views here.

from django.http import HttpResponse
from django.template import loader
 
def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def buscador(request):
    template = loader.get_template('buscador.html')
    context = {}
    return HttpResponse(template.render(context, request))

def article(request):
    template = loader.get_template('article.html')
    articulo = request.GET["articulo"]
    articulos = Article.objects.filter(name__icontains=articulo)
    context = {"articulos": articulos, "query": articulo}
    return HttpResponse(template.render(context, request))

def create_article(request):
    template = loader.get_template('create_article.html')
    form = FormularioArticle()
    if request.method == 'POST':
        form = FormularioArticle(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    context = {'form': form}
    return HttpResponse(template.render(context, request))
