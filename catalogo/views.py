from django.shortcuts import redirect, render
from catalogo.models import linea, producto, encargo
from catalogo.forms import EncargoForm
import datetime
# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404

def detalle(request, id):
    prod = get_object_or_404(producto, id=id, disponibilidad=True)
    return render(request, 'detalle.html', {'producto': prod})

def index(request):
    productos = producto.objects.filter(disponibilidad=True).select_related('linea')
    q = request.GET.get('q', '').strip()
    linea_id = request.GET.get('linea', '')
    if q:
        productos = productos.filter(nombre__icontains=q)
    if linea_id.isdigit():
        productos = productos.filter(linea_id=linea_id)
    return render(request, 'index.html', {
        'productos': productos,
        'lineas': linea.objects.all(),
        'q': q,
        'linea_sel': linea_id,
    })

def boleta(request, id):
    venta = encargo.objects.get(id=id)
    data = {
        'venta': venta
    }
    return render(request, 'boleta.html', data)

def encargar(request, id):
    prod = get_object_or_404(producto, id=id, disponibilidad=True)
    form = EncargoForm(request.POST or None, producto=prod)
    if request.method == 'POST' and form.is_valid():
        enc = form.save(commit=False)
        enc.producto = prod
        enc.save()
        return redirect('boleta', id=enc.id)
    return render(request, 'encargar.html', {'producto': prod, 'form': form})