from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from .serializers import OrderSerializer
from .models import Order
from .utls import validated_user_session
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['POST'])
def addOreder(request, id, token):
    if not validated_user_session(id, token):
        return JsonResponse({'error':'please login frist'})
    if request.method == 'POST':
        # usr_id = id
        amount = request.POST['amount']
        products = request.POST['products']

        total_pro = len(products.split(',')[:-1])

        UserModel = get_user_model()

        try:
            usr = UserModel.objects.get(pk=id)
        except UserModel.DoesNotExist:
            return JsonResponse({'error':'User Does Not Exist'})

        ordr = Order()
        ordr.owner = usr
        ordr.product_names = products
        ordr.total_count = total_pro
        ordr.total_amount = amount
        ordr.save()

        return JsonResponse({'success':True, 'error':False, 'msg':'Order placed sucessfully'})


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all().order_by("id")
    serializer_class = OrderSerializer