from re import S
from rest_framework import serializers
from .models import Order
from api.user.serializers import UserSerializer

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.StringRelatedField(many=False)
   
    class Meta:
        model = Order
        fields = ('product_names', 'total_count', 'total_amount','owner' )
        
        