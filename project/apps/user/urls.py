from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('shopping-car/', views.shopping_car),
    path('orders/', views.orders),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('validate-login', views.validate_login, name='validate-login'),
]
