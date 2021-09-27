from django.urls import path, include
from .views import home
from rest_framework.authtoken import views

urlpatterns = [

    path('', home , name='home'),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('user/', include('api.user.urls')),
    path('order/', include('api.order.urls')),
    path('api-auth-token/', views.obtain_auth_token, name = 'api-auth-token')
]