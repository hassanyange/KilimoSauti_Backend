from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,  get_object_or_404,redirect
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token 
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import CustomUser
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .forms import CustomUserForm


def Home(request):
        return render(request, 'accounts/base.html')
    
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = CustomUser.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key, "user": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  

@api_view(['POST'])
def user_login(request):
    user = get_object_or_404(CustomUser, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(instance=user)
    token, created = Token.objects.get_or_create(user=user)
    response_data = {
        'user': serializer.data,
        'token': token.key  # Include the token key in the response
    }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request.user.email))

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_users(request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


def register_page(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts/base.html')  # Replace 'success_page' with the URL name for the success page
    else:
        form = CustomUserForm()
    return render(request, 'accounts/register.html', {'form': form})

def Endpoints(request):
        return render(request, 'accounts/endpoints.html')