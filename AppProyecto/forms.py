from django import forms

class BandasFormulario (forms.Form):

    nombre = forms.CharField()
    genero = forms.IntegerField()


class DiscosFormulario (forms.Form):

    nombre = forms.CharField(max_length=40)
    banda = forms.CharField(max_length=40)
    año = forms.EmailField()
    genero = forms.CharField(max_length=40)



