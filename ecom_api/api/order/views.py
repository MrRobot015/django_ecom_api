from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from .serializers import OrderSerializer
from .models import Order


# Create your views here.
