from rest_framework import routers, urlpatterns
from django.urls import path , include
from . import views


router = routers.DefaultRouter()
router.register(r'',views.OrderViewSet)

urlpatterns = [

    path('add/<str:id>/<str:token>/', views.addOreder, name='add_order'),
     path('', include(router.urls))
]