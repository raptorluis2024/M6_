from django.shortcuts import render,loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

from django.http import HttpResponse

def sign_up(request):
    template = loader.get_template('sign_up.html')
    if request.method == "GET":
        context = {'form': UserCreationForm}
        return HttpResponse(template.render(context, request))
    else:
        if request.POST["password1"] == request.POST["password2"]:
            usuario = request.POST["username"]
            clave = request.POST["password1"]
            try:
                user = User.objects.create_user(username=usuario, password=clave)
                user.save()
                users = User.objects.all()
                context={"error":"Usuario creado satisfactoriamente",'form': UserCreationForm,"users":users}
                return HttpResponse(template.render(context, request))
            except Exception as ex:
                context={"error":ex,'form': UserCreationForm}
                return HttpResponse(template.render(context, request))
        else:
            context={"error":"Las contraseñas no coinciden",'form': UserCreationForm}
            return HttpResponse(template.render(context, request))