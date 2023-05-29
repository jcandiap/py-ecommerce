from django.urls import path
from store import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail', views.detail, name='detail'),
    path('category-maintainer', views.category_maintainer, name='category_maintainer'),
    path('category-delete', views.category_delete, name='category_delete'),
    path('product-maintainer', views.product_maintainer, name='product_maintainer'),
    path('product-delete', views.product_delete, name='product_delete')
]
