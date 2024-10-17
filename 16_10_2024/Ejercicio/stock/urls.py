from django.urls import path
from . import views


urlpatterns=[
  path('stock/<str:bodega>',views.revisar)
]