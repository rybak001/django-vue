from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Post

class PostSerializer(ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
      return obj.author.username

    class Meta:
        model = Post
        fields = ['title','author','body','pk']