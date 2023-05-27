from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('shopping-car/', views.shopping_car),
    path('orders/', views.orders)
]
