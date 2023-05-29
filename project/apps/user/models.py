from django.db import models
from uuid import uuid4 as uuid

class Country(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid, editable=False)
    name = models.CharField(max_length=50)
# Create your models here.
class User(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    avatar = models.CharField(max_length=300)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)