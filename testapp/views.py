from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import Permission
from rest_framework.authtoken.models import Token
from django.http.response import JsonResponse
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.permissions import IsAdminUser
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import random
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

from django.core.cache import cache


class RegistrationView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = RegistrationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
                
                #user=Registration.objects.get(username=serializer.data['username'])
                # refresh = RefreshToken.for_user(user)
                # return Response({'status':200,'payload':serializer.data,'refresh':str(refresh)

                                #  'access': str(refresh.access_token),'message':'your data is saved'})
            else:
                return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message': 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                username = serializer.data['username']
                password = serializer.data['password']
                register = Registration.objects.filter(
                    username=username).first()
                if register:
                    if username and password:
                        user = authenticate(
                            username=username, password=password)
                        if user:
                            # return JsonResponse(register,safe=False)
                            s = RegistrationSerializer(register)
                            refresh = RefreshToken.for_user(user)
                            return Response({'status':200,"data":serializer.data,'refresh':str(refresh),

                                 'access': str(refresh.access_token),'message':'Login Sucessfully'})
                            
                        else:                        
                            return Response({'message': 'Invalid username and password'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                    else:
                        return Response({
                            'message': 'username and password required'
                        }, status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)






