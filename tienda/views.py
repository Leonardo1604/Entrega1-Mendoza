from django.shortcuts import redirect, render

from .forms import ProductoFormulario, ProductoBusqueda
from .models import Producto

# Create your views here.

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoFormulario(request.POST)
        
        if form.is_valid():
            data=form.cleaned_data
            producto = Producto(nombre=data['nombre'], marca=data['marca'], precio=data['precio'], codigoProducto=data['codigoProducto'], cantidad=data['cantidad'])
            producto.save()
            # return render(request, "index/plantilla.html",{})
            return redirect('index')
        
    form = ProductoFormulario()
    return render(request,'tienda/crear_producto.html', {'form': form})   

def lista_productos(request):
    
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar is not None:
        productos = Producto.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        productos = Producto.objects.all()
    
    form = ProductoBusqueda()
    return render(request,'tienda/lista_productos.html', {'form': form, 'productos': productos})