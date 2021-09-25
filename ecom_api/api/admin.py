from django.contrib import admin
from .category.models import Category
from .product.models import Product

# Register your models here.

    # Register (category app) models here.
admin.site.register(Category)

    # Register (prodouct app) models here.
admin.site.register(Product)