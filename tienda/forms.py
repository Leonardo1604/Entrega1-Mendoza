from django import forms

from tienda.models import Producto

class ProductoFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=25)
    marca = forms.CharField(max_length=30)
    precio = forms.DecimalField(max_digits=100, decimal_places=2)
    codigoProducto = forms.IntegerField()
    cantidad = forms.IntegerField()

class ClienteFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=25)
    apellido = forms.CharField(max_length=30)
    dni = forms.IntegerField()
    
    
class VendedorFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=25)
    apellido = forms.CharField(max_length=30)
    codigoEmpleado = forms.IntegerField()
    empleado = forms.BooleanField(required=False)
    
class ProductoBusqueda(forms.Form):
    nombre = forms.CharField(max_length=25)