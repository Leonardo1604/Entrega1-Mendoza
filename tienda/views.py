from django.shortcuts import redirect, render

from .forms import ProductoFormulario, ProductoBusqueda, ClienteFormulario, VendedorFormulario
from .models import Cliente, Producto, Vendedor

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
        
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteFormulario(request.POST)
        
        if form.is_valid():
            data=form.cleaned_data
            cliente = Cliente(nombre=data['nombre'], apellido=data['apellido'], dni=data['dni'])
            cliente.save()
            # return render(request, "index/plantilla.html",{})
            return redirect('index')
    
    form = ClienteFormulario()
    return render(request,'tienda/crear_cliente.html', {'form': form})   
        
def crear_vendedor(request):
    if request.method == 'POST':
        form = VendedorFormulario(request.POST)
        
        if form.is_valid():
            data=form.cleaned_data
            vendedor = Vendedor(nombre=data['nombre'], apellido=data['apellido'], codigoEmpleado=data['codigoEmpleado'], empleado=data['empleado'])
            vendedor.save()
            # return render(request, "index/plantilla.html",{})
            return redirect('index')
        
    form = VendedorFormulario()
    return render(request,'tienda/crear_vendedor.html', {'form': form})   

def lista_productos(request):
    
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar is not None:
        productos = Producto.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        productos = Producto.objects.all()
    
    form = ProductoBusqueda()
    return render(request,'tienda/lista_productos.html', {'form': form, 'productos': productos})