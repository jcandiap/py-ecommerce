from django.http import HttpResponse
from django.shortcuts import render

app_name = 'user'
# Create your views here.
def profile(request):
    return HttpResponse("Vista de perfil!")

def shopping_car(request):
    return HttpResponse("Vista de carrito de compras!")

def orders(request):
    return HttpResponse("Vista de las ordenes de compra!")

def login(request):
    return render(request, 'user/login_user.html')

def register(request):
    return render(request, 'user/register_user.html')