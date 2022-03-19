

from django.urls import path
from . import views

urlpatterns = [
    path('producto/nuevo/', views.crear_producto,name="crear_producto"),
    path('producto/',views.lista_productos,name="lista_productos")
]
