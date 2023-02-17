from django.contrib import admin
from .models import BlogPost
# Register your models here.

class CustomBlogPostAdmin(admin.ModelAdmin):
    model = BlogPost
    list_display = ('title','author','updated_on','content','status')
    list_filter = ('author',)
    search_fields = ('author',)
    ordering = ('title',)

admin.site.register(BlogPost, CustomBlogPostAdmin)