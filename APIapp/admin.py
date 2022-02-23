from django.contrib import admin
from .models import Category, Product, Book, Cart


admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Product)
admin.site.register(Cart)
