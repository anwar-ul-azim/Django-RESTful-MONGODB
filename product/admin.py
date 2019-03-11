from django.contrib import admin
from .models import Product, Seller, SubCategory, Category, Customer

admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Customer)
