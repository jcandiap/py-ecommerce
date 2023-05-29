from django import forms

class CategoryForm(forms.Form):
    category = forms.CharField(max_length=100)
    
class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200)
    stock = forms.IntegerField()
    image = forms.CharField(max_length=300)
    price = forms.IntegerField()
    category = forms.CharField()