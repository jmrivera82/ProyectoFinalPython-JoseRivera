from django import forms


class EquiposFormulario (forms.Form):

    nombre = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=40)
    año = forms.EmailField()
    campaña = forms.CharField(max_length=40)



