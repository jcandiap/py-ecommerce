from django.http import HttpResponse
from django.shortcuts import render

app_name = 'store'

# Create your views here.
def index(request):
    return render(request, 'store/index_store.html')

def detail(request):
    return HttpResponse("Vista de detalle!")