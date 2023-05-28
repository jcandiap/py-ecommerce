from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import User

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
        if __check_password(password):
            message = f'Inicio exitoso, bienvenido(a) { user.name } { user.last_name }'
            return JsonResponse({ 'message': message })
    except Exception:
        return JsonResponse({ 'error': 'Usuario no se encuentra registrado' })
    return JsonResponse({ 'error': 'Datos no coinciden para verificar al usuario' })

def __check_password(user: User, password: str):
    if user.password == password:
        return True
    return False