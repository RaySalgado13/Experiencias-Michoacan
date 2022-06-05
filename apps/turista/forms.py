from django import forms 
from apps.home.models import Reservacion

CANTIDAD_ELECCIONES_PRODCUTO = [(i, str(i)) for i in range(1, 21)]

class CarroAddProcutoForm(forms.Form):
    cantidad = forms.TypedChoiceField(
            choices = CANTIDAD_ELECCIONES_PRODCUTO,
            coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)


class ReservacionCreateForm(forms.ModelForm):
        class Meta:
                model = Reservacion
                fields = ['nombre', 'email', 'telefono']