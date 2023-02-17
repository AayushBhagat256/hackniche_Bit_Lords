from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('bloglist/', views.BlogPostList.as_view(), name='ListOfBlog'),
    path('blogdetail/<slug:pk>/', views.BlogDetail.as_view(), name='DetailOfBlog'),
]


urlpatterns = format_suffix_patterns(urlpatterns)