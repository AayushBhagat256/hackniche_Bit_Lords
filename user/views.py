from django.shortcuts import render

# Create your views here.
from .models import UserProfile,CodeEmail
from rest_framework.generics import GenericAPIView
from .serializers import RegistrationSerializer, CodeSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import logout
from rest_framework.parsers import FileUploadParser,FormParser,MultiPartParser

class Registration(GenericAPIView):
    permission_classes=[AllowAny]
    serializer_class = RegistrationSerializer
    
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            print(type(account))
            token= Token.objects.get(user=account).key
            data['serializer_data']=serializer.data
            data['token']=token
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CodeView(GenericAPIView): 
    permission_classes=[AllowAny]
    serializer_class = CodeSerializer
    def post(self, request):
        serializer = CodeSerializer(data=request.data)
        if serializer.is_valid():
            if CodeEmail.objects.filter(code = serializer.validated_data['code'] , email= serializer.validated_data['email']).exists()  :
                user=UserProfile.objects.get(email=serializer.validated_data['email'])
                user.is_active = True
                user.save()
                return Response('Email successfully confirmed')
            else:
                return Response({'message':'not equal'})
        else:
            print(serializer.errors)
            return Response({'message': 'Serializer is not valid'})


class User_logout(GenericAPIView): 
    permission_classes=[IsAuthenticated]
    def get(self,request):
        logout(request)
        return Response('User Logged out successfully')  


class Profile(GenericAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = ProfileSerializer
    parser_classes = (FormParser, MultiPartParser)

    def get_object(self,request):
            try:
                return UserProfile.objects.get(pk=request.user)
            except UserProfile.DoesNotExist:
                raise status.HTTP_404_NOT_FOUND

    def get(self, request):
        user = self.get_object(request)
        serializer = ProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def put(self, request):
        user = self.get_object(request)
        serializer = ProfileSerializer(user, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  