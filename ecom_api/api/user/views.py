from django.contrib.auth.backends import UserModel
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login , logout
import re 
from .serializers import UserSerializer
from .models import CustomUser
from .utls import generate_session_token
 

# Create your views here.
@csrf_exempt
def signin(request):
    """validate and check auth for user signin"""
  
    if not request.method == 'POST':
        return JsonResponse({'error':'send a post request with valid data only'})
    
    username = request.POST['username']
    # if username == None:
    #     email = request.POST['email']
    
    password = request.POST['password']
        #========validation part=============#
    # if not re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', email):
    #     return JsonResponse({'error':'enter a valid username'})
    
    if len(password) < 5:
        return JsonResponse({'error':'password to short'})
    
    if len(username) > 15:
        return JsonResponse({'error':'username is to long'})

        #======================================#

    
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(username = username)

        if user.check_password(password):
            usr_dict = UserModel.objects.filter(username= username).values().first()
            usr_dict.pop('password') # remove the password from the dict for security of it

            if user.session_token != '0':
                user.session_token = '0'
                user.save()
                return JsonResponse({'error':'Previous session exists'})
            # generating session_token
            token = generate_session_token()
            user.session_token = token 
            user.save()

            login(request, user)
            return JsonResponse({'token':token, 'user': usr_dict})

        else:
            return JsonResponse({'error':'Invalid password'})

    except UserModel.DoesNotExist:
        return JsonResponse({'error':'Invalid email'})

    #====================================#
@csrf_exempt
def signout(request, id):
    """logout and remove the session_token"""
    logout(request)

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user ID'})

    return JsonResponse({'success': 'Logout success'})

    #====================================#


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]