from re import S
from rest_framework import serializers
from .models import Order
from api.user.serializers import UserSerializer

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    owner = UserSerializer()
    product_names = serializers.CharField(max_length=500)
    total_count = serializers.IntegerField()
   
    total_amount =  serializers.CharField(max_length=500)
    class Meta:
        model = Order
        fields = '__all__'
        
        