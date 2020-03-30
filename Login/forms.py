from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LoginUser(forms.Form):

    username = forms.CharField(label="Nombre de usuario", help_text="Ingrese un nombre su nombre de usuario", max_length=8, required=True, widget=forms.TextInput(attrs={
        "placeholder":"Nombre de usuario"
    }))

    password= forms.CharField(label="Contraseña", help_text="Ingrese su contraseña", required=True, widget=forms.TextInput(attrs={
        "placeholder":"Ingrese su contraseña"
    }))

    def clean_username(self):
        username = str.lower(self.cleaned_data["username"])
        if not User.objects.filter(username=username).exists():
            raise ValidationError("El usuario no existe")
        return username
    
    def clean_password(self):
        username = self.data["username"]
        password = self.cleaned_data["password"]
        user = User.objects.filter(username=username).first()
        if user and not user.check_password(password):
            raise Validation("Contraseña incorrecta")
        return password
        