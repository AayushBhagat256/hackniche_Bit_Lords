from django.shortcuts import render

# Create your views here.
from .serializers import BlogSerializer
from .models import BlogPost
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response

class BlogPostList(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer

    def get(self, request):
        blogs = BlogPost.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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

    def delete(self, request, pk):
        blog=self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)