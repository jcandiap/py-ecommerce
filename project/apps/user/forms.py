from django import forms

class RegisterForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    avatar = forms.CharField(max_length=300)
    email = forms.EmailField()
    confirm_email = forms.EmailField()
    password = forms.CharField(max_length=100)
    confirm_password = forms.CharField(max_length=100);
    pais = forms.CharField(max_length=100)
    
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100)
    
class CountryForm(forms.Form):
    country = forms.CharField(max_length=100)