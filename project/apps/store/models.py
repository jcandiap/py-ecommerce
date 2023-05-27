from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    stock = models.DecimalField(default=1, decimal_places=0, max_digits=3)
    image = models.CharField(max_length=300)
    price = models.DecimalField(default=1, decimal_places=0, max_digits=8)
    
class Gallery(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.CharField(max_length=300)
    