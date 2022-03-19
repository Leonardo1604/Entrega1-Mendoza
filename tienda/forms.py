from django import forms

from tienda.models import Producto

class ProductoFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=25)
    marca = forms.CharField(max_length=30)
    precio = forms.DecimalField(max_digits=100, decimal_places=2)
    codigoProducto = forms.IntegerField()
    cantidad = forms.IntegerField()
    
class ProductoBusqueda(forms.Form):
    nombre = forms.CharField(max_length=25)