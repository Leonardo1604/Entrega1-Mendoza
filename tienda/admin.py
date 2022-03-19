from django.contrib import admin

from tienda.models import Cliente, Producto, Vendedor

# Register your models here.
admin.site.register(Producto)
admin.site.register(Vendedor)
admin.site.register(Cliente)