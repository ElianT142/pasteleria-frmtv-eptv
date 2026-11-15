from django.shortcuts import render
from catalogo.models import linea, producto, encargo
# Create your views here.

def index(request):
    productos = producto.objects.all()
    data = { 
        'titulo': 'Pastelería FRMTV',
        'mensaje': 'Bienvenidos a la pastelería FRMTV',
        'productos': productos
    }
    return render(request, 'index.html', data)