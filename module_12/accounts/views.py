from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer
from .models import CustomUser
import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv('.env')

os.environ['SECRET_KEY'] = os.getenv('SECRET_KEY')

class RegisterView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = CustomUser.objects.filter(email=email).first()

        if user is None or not user.check_password(password):
            return Response(
                data={'error': 'Invalid email or password'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        payload = {
            'id': user.id,
            'email': user.email,
            'exp': datetime.now() + timedelta(hours=1),
            'iat': datetime.now()
        }
        token = jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm='HS256')

        response =Response()
        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data ={
            'message': 'Login successful',
            'token': token
        }

        return response
