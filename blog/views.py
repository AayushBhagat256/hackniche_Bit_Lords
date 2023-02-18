from django.shortcuts import render

# Create your views here.
from .serializers import BlogSerializer
from .models import BlogPost,UserProfile
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser,FormParser,MultiPartParser
from django.http import Http404, HttpResponse, HttpResponseForbidden

class BlogPostList(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer
    parser_classes = (FormParser, MultiPartParser)

    def get(self, request):
        blogs = BlogPost.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        file_obj = request.FILES['picture']
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            inst = serializer.save()
            inst.picture = file_obj
            inst.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class BlogDetail(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer

    def get_object(self, pk):
        try:
            return BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def put(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_user(self, pk):
        try:
            return UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    # def delete(self, request, pk):
       
    #     if blog.author == re
    #     blog=self.get_object(pk)
    #     blog.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


    def delete(self, request, pk):
        user = request.user
        blog = self.get_object(pk)
        print(request.user)
        print(blog.author)
        if blog.author == user:
            blog.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)