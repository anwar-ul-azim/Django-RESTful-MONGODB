from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=50, default='Category')

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=50, default='Sub-Category')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, default='Product')
    details = RichTextField(max_length=100, default='Product Details')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Category')
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    sells = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length=50, default='Name')
    email = models.EmailField(max_length=100, unique=True)
    phone = models.IntegerField()
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50, default='Name')
    email = models.EmailField(max_length=100, unique=True)
    phone = models.IntegerField()
    address = models.CharField(max_length=200, default='Address')
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name