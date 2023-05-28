from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Category

app_name = 'store'

# Create your views here.
def index(request):
    products = __find_products(request)
    categories = Category.objects.all()
    data = { 'products': products, 'categories': categories }
    return render(request, 'store/index_store.html', data)

def detail(request):
    id = request.GET.get('id')
    try:
        product = Product.objects.get(id = id)
    except:
        return redirect('/')
    data = { 'product': product }
    return render(request, 'store/product_detail.html', data)

def __find_products(request):
    try:
        category = request.GET.get('category')
        if category:
            return Product.objects.filter(category=category)
        else:
            return Product.objects.all()
    except:
        return Product.objects.all()