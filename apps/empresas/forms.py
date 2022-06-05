import email
from pyexpat import model
from django import forms
from apps.home.models import Empresa, Imagen, Producto, Reservacion, Tipo_producto, Paquete

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
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "",
                "class": "form-control",
                "type":"date"
            }
        ), required=False)
    
    fecha_fin = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "",
                "class": "form-control",
                "type":"date"
            }
        ), required=False)
    
    stock = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Disponibilidad",
                "class": "form-control"
            }
        ),required=False)
    
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


class ReservacionForm(forms.ModelForm):
    
    nombre = forms.CharField(
        widget=forms.TimeInput(
            attrs={
                "placeholder": "Nombre del cliente",
                "class": "form_control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form_control"
            }
        ))
    telefono = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Numero de telefono",
                "class": "form_control"
            }
        ))
    status = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Status del pago",
                "class": "form_control"
            }
        ))
    producto = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "form_control"
            }
        ))

    class Meta:
        model = Reservacion
        fields = ['nombre','email','telefono','status','producto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs.update({
            "class": "form-control"
        })
        self.fields['email'].widget.attrs.update({
            "class": "form-control"
        })
        self.fields['telefono'].widget.attrs.update({
            "class": "form-control"
        })
        self.fields['status'].widget.attrs.update({
                "class": "form-control"
        })



class PaqueteForm(forms.ModelForm):

    class Meta:
        model = Paquete
        
        exclude = ('empresa',)


    def __init__(self, empresa, *args,**kwars):
        super(PaqueteForm, self).__init__( *args, **kwars)
        self.fields['producto'].queryset = Producto.objects.filter(empresa=empresa)

    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre del paquete",
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
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "",
                "class": "form-control",
                "type":"date"
            }
        ), required=False)
    
    fecha_fin = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "",
                "class": "form-control",
                "type":"date"
            }
        ), required=False)
    
    stock = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Disponibilidad",
                "class": "form-control"
            }
        ),required=False)

    producto = forms.ModelMultipleChoiceField(
    
        queryset=Producto.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "form_control"
            }
        ))

        

       

    
    

    