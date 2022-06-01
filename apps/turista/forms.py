from django import forms 

CANTIDAD_ELECCIONES_PRODCUTO = [(i, str(i)) for i in range(1, 21)]

class CarroAddProcutoForm(forms.Form):
    cantidad = forms.TypedChoiceField(
            choices = CANTIDAD_ELECCIONES_PRODCUTO,
            coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)