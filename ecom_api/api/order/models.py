from functools import total_ordering
from django.db import models
from api.user.models import CustomUser
from api.product.models import Product
import uuid

# Create your models here.

class Order(models.Model):
    owner= models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    product_names = models.CharField(max_length=500)
    total_count = models.IntegerField(default=0 , null=True , blank=True)
    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    total_amount =  models.CharField(max_length=500, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


   