from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.Registration.as_view(), name='register'),
    path('loginview/', views.LoginAPIView.as_view(), name='loginview'),
    path('login/', obtain_auth_token, name='login'),
    path('register/verify/', views.CodeView.as_view(), name='register'),
    path('logout/', views.User_logout.as_view(), name='logout'),
    path('profile/', views.Profile.as_view(), name='profile')
]

urlpatterns = format_suffix_patterns(urlpatterns)