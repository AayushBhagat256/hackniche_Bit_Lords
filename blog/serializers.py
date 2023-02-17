from rest_framework import serializers
from .models import BlogPost
from user.models import UserProfile
import datetime

class BlogSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        queryset=UserProfile.objects.all(),
        slug_field='email'
    )
    class Meta:
        model = BlogPost
        fields = '__all__'

    def save(self):
        # user =self.validated_data['author']
        blog_inst = BlogPost(
            title = self.validated_data['title'],
            author = self.validated_data['author'],
            content=self.validated_data['content'],
            status=self.validated_data['status'],
            updated_on=datetime.datetime.now()
        )
        blog_inst.save()