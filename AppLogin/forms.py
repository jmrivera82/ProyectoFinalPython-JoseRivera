
#from dataclasses import field
from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class AuthenticationFormLogin(AuthenticationForm):
   # email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'autofocus': True}))
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email']



class UsuarioRegistroForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}


class UsuarioEdicionForm(UserCreationForm):
   
    email = forms.EmailField(label="Modificar E-mail")
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repita la contraseña antigua', widget=forms.PasswordInput)

    
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}      