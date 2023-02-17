from django.db import models

# Create your models here.
from user.models import UserProfile


class BlogPost(models.Model):
    
    STATUS = (
        (0,"Draft"),
        (1,"Publish")
    )

    title = models.CharField(max_length=200, unique=True, primary_key=True)
    author = models.ForeignKey(UserProfile, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(blank=True,)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.Title