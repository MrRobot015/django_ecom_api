from functools import total_ordering
from django.db import models
from api.user.models import CustomUser
from api.product.models import Product
import uuid

# Create your models here.

class Order(models.Model):
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    product_names = models.ManyToManyField('product', blank=True)
    total_count = models.CharField(max_length=500, default=0)
    transaction_id = models.UUIDField(default=uuid.uuid3, unique=True, editable=False)
    total_amount =  models.IntegerField(default=0 , null=True , blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    @property
    def getTotalCount(self):
        """this method update the the review total and ratio after submiting a new review"""
        total_amount = self.product_names.count()
        self.total_amount = total_amount
        self.save()