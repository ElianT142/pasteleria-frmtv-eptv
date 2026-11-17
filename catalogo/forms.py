from django import forms
from django.utils import timezone
from catalogo.models import encargo

class EncargoForm(forms.ModelForm):
    class Meta:
        model = encargo
        fields = ['nombre', 'correo', 'fecha_retiro', 'cantidad']
        widgets = {'fecha_retiro': forms.DateInput(attrs={'type': 'date'})}

    def __init__(self, *args, producto=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.producto = producto
        for campo in self.fields.values():
            campo.widget.attrs['class'] = 'form-control'

    def clean_fecha_retiro(self):
        fecha = self.cleaned_data['fecha_retiro']
        if fecha < timezone.localdate():
            raise forms.ValidationError('La fecha de retiro no puede ser anterior a hoy.')
        return fecha

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if not 1 <= cantidad <= 3:
            raise forms.ValidationError('La cantidad debe estar entre 1 y 3.')
        if self.producto and cantidad > self.producto.stock_dia:
            raise forms.ValidationError(
                f'Solo quedan {self.producto.stock_dia} unidades disponibles.')
        return cantidad
