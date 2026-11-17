from django.shortcuts import redirect, render
from catalogo.models import linea, producto, encargo
from catalogo.forms import FormVentas
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
    prod = producto.objects.get(id=id)
    form = FormVentas()
    form.fields['id_encargo'].initial = id

    if request.method == 'POST':
        form = FormVentas(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']
            prod.stock_dia -= cantidad
            prod.cantidad -= cantidad

        if prod.stock_dia <= 0 or prod.cantidad <= 0:
            prod.stock_dia = 0
            prod.cantidad = 0
            prod.disponibilidad = False

            prod.save()

            venta = encargo()
            venta.producto = prod
            venta.nombre = form.cleaned_data['cliente']
            venta.correo = form.cleaned_data['correo']
            venta.fecha_retiro = form.cleaned_data['fecha_retiro']
            venta.cantidad = cantidad
            venta.codigo = form.cleaned_data['codigo']



            valor_producto = prod.precio
            total_original = venta.cantidad * valor_producto

            venta.total_original = total_original
            venta.save()

            return redirect('/boleta/' + str(venta.id))

    data = {
        'producto': prod,
        'form': form
    }
    return render(request, 'encargar.html', data)
