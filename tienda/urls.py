

from django.urls import path
from . import views

urlpatterns = [
    path('producto/nuevo/', views.crear_producto,name="crear_producto"),
    path('cliente/nuevo/', views.crear_cliente,name="crear_cliente"),
    path('vendedor/nuevo/', views.crear_vendedor,name="crear_vendedor"),
    path('producto/',views.lista_productos,name="lista_productos")
    
]
