from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=255, null=True)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    stock = models.IntegerField()