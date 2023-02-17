from rest_framework import serializers
from .models import UserProfile,CodeEmail

import smtplib
from email.mime.text import MIMEText
from hacknicheproject.settings import EMAIL_HOST_USER,EMAIL_HOST_PASSWORD
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from rest_framework.authtoken.models import Token

import random

class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model=UserProfile
        fields = ['email','username','password','password2','soldier','fname','lname','contact_no','bio','served_with','start_of_service','end_of_service']
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def save(self):
        profile = UserProfile(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        profile.set_password(password)
        profile.is_active=False

        profile.save()
        
        cd=random.randint(10000, 99999)
        profile_code = CodeEmail(
            email=self.validated_data['email'],
            code=cd,
        )
        profile_code.save()

        mess=f'{cd}'
        send_mail(
            subject='Email verification',
            message=("This mail is to verify your mail.TO verify code is:"+mess),
            from_email=EMAIL_HOST_USER,
            recipient_list=[profile,]
        )

        return profile
    

class CodeSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    email  = serializers.EmailField()
