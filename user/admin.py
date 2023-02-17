from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class CustomUserAdmin(UserAdmin):
    model = UserProfile
    list_display = ('email','username','is_superuser','is_staff','is_active','soldier','Profilepic','fname')
    list_filter = ('is_staff','soldier')
    search_fields = ('email','username','soldier')
    ordering = ('email','username')

UserProfile = get_user_model()
admin.site.register(UserProfile, CustomUserAdmin)