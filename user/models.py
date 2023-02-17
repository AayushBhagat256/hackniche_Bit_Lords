from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class UserProfile(AbstractBaseUser, PermissionsMixin):

    SERVED_WITH_CHOICES = [
        ('AY', 'Army'),
        ('NY', 'Navy'),
        ('AR', 'Air Force'),
    ]

    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,error_messages={'unique': "A user with that email already exists.",})
    username = models.CharField( max_length=150, unique=True,error_messages={'unique': "A user with that username already exists.",} )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    soldier = models.BooleanField(default=False)

    fname = models.CharField(blank=True, max_length=20)
    lname = models.CharField(blank=True, max_length=20)
    contact_no = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True)
    served_with = models.CharField(max_length=2, choices=SERVED_WITH_CHOICES, null=True)
    start_of_service = models.DateTimeField(blank=True, null=True)
    end_of_service = models.DateTimeField(blank=True, null=True)
    Profilepic = models.FileField(upload_to='user_profile/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class CodeEmail(models.Model):
    code = models.IntegerField()
    email = models.EmailField(max_length=254)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)