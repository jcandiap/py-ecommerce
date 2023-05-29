from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import CategoryForm, ProductForm

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

def category_maintainer(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form_info = form.cleaned_data
            category = Category(name = form_info["category"])
            category.save()
    categories = Category.objects.all()
    return render(request, 'store/category_maintainer.html', { 'added_categories': categories })

def category_delete(request):
    id = request.GET.get('id')
    try:
        category = Category.objects.get(id = id)
        category.delete()
    except:
        return redirect('/')
    return redirect('/category-maintainer')

def product_maintainer(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            print('VALIDO!')
            try:
                form_info = form.cleaned_data
                category = Category.objects.get(id = form_info["category"])
                product = Product(
                    name = form_info["name"], 
                    description = form_info["description"], 
                    stock = form_info["stock"], 
                    image = form_info["image"], 
                    price = form_info["price"], 
                    category = category)
                product.save()
            except Exception as e:
                print(e)
    products = Product.objects.all()
    return render(request, 'store/product_maintainer.html', { 'added_products': products, 'product_categories': categories })

def product_delete(request):
    id = request.GET.get('id')
    try:
        product = Product.objects.get(id = id)
        product.delete()
    except:
        return redirect('/')
    return redirect('/product-maintainer')

def __find_products(request):
    try:
        category = request.GET.get('category')
        if category:
            return Product.objects.filter(category=category)
        else:
            return Product.objects.all()
    except:
        return Product.objects.all()