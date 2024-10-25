from django.shortcuts import render,loader,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import Formulario_Tarea
from .models import Tarea

def crear_tarea1(request):
    template = loader.get_template('crear_tarea.html')
    context = {'form':Formulario_Tarea}
    return HttpResponse(template.render(context, request))


def detalle_tarea(request, tarea_id):
    #tarea = Tarea.objects.get(pk=tarea_id)
    if request.method == 'GET':
        template = loader.get_template('detalle_tarea.html')
        tarea = get_object_or_404(Tarea, pk=tarea_id)
        form = Formulario_Tarea(instance=tarea)
        context = {'tarea': tarea, 'form':form}
        return HttpResponse(template.render(context, request))
    else:
        try:
            tarea = get_object_or_404(Tarea, pk=tarea_id)
            form = Formulario_Tarea(request.POST, instance=tarea)
            #form = Formulario_Tarea(instance=tarea)
            form.save()
            return redirect("tareas")
        except:
            template = loader.get_template('detalle_tarea.html')
            context = {'tarea':tarea,'form':form, 'error':"Error al modificar la tarea"}
            return HttpResponse(template.render(context, request))

def borrar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    tarea.delete()
    return redirect('tareas')

def crear_tarea(request):
    if request.method == 'GET':
        return render(request, 'crear_tarea.html', {'form': Formulario_Tarea})
    else:
        try:
            form = Formulario_Tarea(request.POST)
            nueva_tarea = form.save(commit=False)
            nueva_tarea.user = request.user
            nueva_tarea.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'crear_tarea.html', {'form': Formulario_Tarea,'error': 'Ingresa datos válidos en la tarea'})





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
                login(request,user)
                return redirect("/tareas/")
                #context={"error":"Usuario creado satisfactoriamente",'form': UserCreationForm,"users":users}
                #return HttpResponse(template.render(context, request))
            except Exception as ex:
                context={"error":ex,'form': UserCreationForm}
                return HttpResponse(template.render(context, request))
        else:
            context={"error":"Las contraseñas no coinciden",'form': UserCreationForm}
            return HttpResponse(template.render(context, request))
        
@login_required      
def tareas(request):
    template = loader.get_template('tareas.html')
    tareas = Tarea.objects.filter(user=request.user)
    context = {'tareas': tareas}
    return HttpResponse(template.render(context, request))

def sign_out(request):
    logout(request)
    return redirect('home')

def log_in(request):
    template = loader.get_template('login.html')
    context = {'form':AuthenticationForm}
    if request.method == "GET":
        return HttpResponse(template.render(context, request))
    else:
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate( request, username=usuario, password=clave)
        if user is None:
            context["error"] = "Usuario o contraseña incorrectos"
            return HttpResponse(template.render(context, request))
        else:
            login(request, user)
            tareas = Tarea.objects.filter(user=request.user)
            template = loader.get_template('tareas.html')
            #tareas = Tarea.objects.filter(user=request.user)
            usuario = User.objects.filter(username=usuario).values()[0]["username"]
            context = {"usuario_logueado":usuario, "tareas":tareas}
            #context = {"usuario_logueado":usuario,'tareas': tareas}
            return HttpResponse(template.render(context, request))
            #return redirect("tareas")
   
