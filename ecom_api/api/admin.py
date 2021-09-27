from django.contrib import admin
from .category.models import Category
from .product.models import Product
from .user.models import CustomUser
from .order.models import Order

# Register your models here.

    # Register (category app) models here.
admin.site.register(Category)

    # Register (prodouct app) models here.
admin.site.register(Product)

    # Register (prodouct app) models here.
admin.site.register(CustomUser)

    # Register (prodouct app) models here.
admin.site.register(Order)