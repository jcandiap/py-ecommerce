from .models import Category

def datos_globales(request):
    categories = Category.objects.all()
    data = { 'categories': categories }
    return data