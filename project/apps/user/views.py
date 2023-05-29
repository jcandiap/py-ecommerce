from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import User, Country
from .forms import RegisterForm, CountryForm
from django.contrib import messages
from uuid import uuid4 as uuid

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
    countries = Country.objects.all()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form_info = form.cleaned_data
            country = Country.objects.get(id = form_info["pais"])
            user = User(
                id = uuid(), 
                name = form_info["nombre"], 
                last_name = form_info["apellido"], 
                email = form_info["email"], 
                password = form_info["password"], 
                avatar = form_info["avatar"], 
                country = country
            )
            user.save()
            return render(request, 'user/login_user.html')
    else:
        form = RegisterForm()
    return render(request, 'user/register_user.html', { 'form': form, 'countries': countries })

def validate_login(request):
    try:
        if request.method == "POST":
            return __check_login_info(request)
        return JsonResponse({ 'message': 'error al verificar' })
    except Exception as e:
        print(e)
        return JsonResponse({ 'error': e })
    
def __check_login_info(request) -> JsonResponse:
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email is None:
        return JsonResponse({ 'error': 'email es requerido' })
    if password is None:
        return JsonResponse({ 'error': 'password es requerido' })
    try:
        user = User.objects.get(email = email)
        if user is None:
            return JsonResponse({ 'error': 'usuario no encontrado' })
        if __check_password(user, password):
            message = f'Inicio exitoso, bienvenido(a) { user.name } { user.last_name }'
            return JsonResponse({ 'message': message })
    except Exception:
        return JsonResponse({ 'error': 'Usuario no se encuentra registrado' })
    return JsonResponse({ 'error': 'Datos no coinciden para verificar al usuario' })

def __check_password(user: User, password: str):
    if user.password == password:
        return True
    return False

def country_maintainer(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form_info = form.cleaned_data
            country = Country(name = form_info["country"])
            country.save()
    countries = Country.objects.all()
    return render(request, 'user/country_maintainer.html', { 'added_countries': countries })

def country_delete(request):
    id = request.GET.get('id')
    try:
        country = Country.objects.get(id = id)
        country.delete()
    except:
        return redirect('/')
    return redirect('/profile/country-maintainer')