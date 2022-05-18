from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import make_password, check_password
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from .serializers import UserSerializer
from .models import Users
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import login, authenticate
from .authTokenRH import CsrfExemptSessionAuthentication, BasicAuthentication

# Create your views here.
class Login(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self, request):
        username = request.data.get('username', None)            
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_200_OK)
        return Response({'error': 'contraseña o usuario incorrecto'},status=status.HTTP_400_BAD_REQUEST)

class CustomUserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()