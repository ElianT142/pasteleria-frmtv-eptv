
from django import forms
from catalogo.models import encargo
from django.utils import timezone

class FormVentas(forms.Form):
    id_encargo = forms.CharField(widget=forms.HiddenInput)
    cliente = forms.CharField()
    correo = forms.EmailField(required=False)
    fecha_retiro = forms.DateField(widget=forms.SelectDateWidget)
    cantidad = forms.IntegerField(min_value=1, max_value=3)
    codigo = forms.CharField(required=False)

    id_encargo.widget.attrs['class'] = 'form-control'
    cliente.widget.attrs['class'] = 'form-control'
    correo.widget.attrs['class'] = 'form-control'
    fecha_retiro.widget.attrs['class'] = 'form-control'
    cantidad.widget.attrs['class'] = 'form-control'
    codigo.widget.attrs['class'] = 'form-control'
