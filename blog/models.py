from django.db import models

# Create your models here.
from user.models import UserProfile
from django.utils.safestring import mark_safe

class BlogPost(models.Model):
    
    def upload_to(instance, filename):
        return 'user_profile/'.join(['images', str(instance.name), filename])

    STATUS = (
        (0,"Draft"),
        (1,"Publish")
    )

    title = models.CharField(max_length=200, unique=True, primary_key=True)
    author = models.ForeignKey(UserProfile, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(blank=True,)
    status = models.IntegerField(choices=STATUS, default=0)
    picture = models.ImageField(upload_to="user_profile/", null =True, blank=True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title

