"""
URL configuration for gestor_tareas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home
from tareas.views import sign_up,tareas,sign_out,log_in,crear_tarea,detalle_tarea,borrar_tarea


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('sign_up/', sign_up),
    path('tareas/', tareas, name='tareas'),
    path('logout/', sign_out, name='logout'),
    path('login/', log_in, name="login"),
    path('crear_tarea/',crear_tarea),
    path('detalleTarea/<int:tarea_id>', detalle_tarea,
    name="detalleTarea"),
    path('detalleTarea/<int:tarea_id>/delete', borrar_tarea, name="borrarTarea")
    
]
