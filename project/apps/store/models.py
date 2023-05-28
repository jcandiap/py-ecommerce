from django.db import models
from uuid import uuid4 as uuid

class Category(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid)
    name = models.CharField(max_length=100, default='No especificada')
class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    stock = models.IntegerField(default=1)
    image = models.CharField(max_length=300)
    price = models.DecimalField(default=1, decimal_places=0, max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='N/A')
    
class Gallery(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.CharField(max_length=300)