from pyexpat import model
from django import forms
from apps.home.models import Imagen, Producto, Tipo_producto

options_tipo_producto = Tipo_producto.objects.all()

class DateTimePickerInput(forms.DateTimeInput):
        input_type = 'datetime'

class ProductoForm(forms.ModelForm):

    

    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre del producto",
                "class": "form-control"
            }
        ))
    descripcion = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Descripcion del producto",
                "class": "form-control"
            }
        ))
    precio = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Precio",
                "class": "form-control"
            }
        ))
    fecha_inicio = forms.DateTimeField(
        widget=DateTimePickerInput(
            attrs={
                "placeholder": "",
                "class": "form-control",
            }
        ))
    
    fecha_fin = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "",
                "class": "form-control"
            }
        ))
    
    stock = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Disponibilidad",
                "class": "form-control"
            }
        ))
    
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','precio','fecha_inicio','fecha_fin','stock','tipo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['tipo'].widget.attrs.update({
            "class": "form-control"
        })
    

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['image']