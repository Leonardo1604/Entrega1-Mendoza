
from django.shortcuts import render



def index(request):
    return render(request, 'index/index.html', {})

def plantilla(request):
    
    datos ={
        'lista': ['Comestibles', 'Utiles', 'Variedad'],
        'nombre': 'Tienda Juanito',
        'apellido': 'Martinez',
        'email': 'ldmm16@hotmail.com',
        'numero': '968547521'
    }
    return render(request, 'index/plantilla.html', datos)