 



from django import forms 



class juegosFormulario(forms.Form):
    
    nombre= forms.CharField(max_length=40)
    año= forms.IntegerField()
    genero= forms.CharField(max_length=40)
    consola= forms.CharField(max_length=40)
    