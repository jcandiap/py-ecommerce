from django.urls import path
from user import views

urlpatterns = [
    path('', views.profile),
    path('shopping-car/', views.shopping_car),
    path('orders/', views.orders)
]
