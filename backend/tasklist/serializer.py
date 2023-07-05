from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Post, User

class PostSerializer(ModelSerializer):
  author = serializers.SerializerMethodField()

  def get_author(self, obj):
    return obj.author.username

  class Meta:
    model = Post
    fields = ['title','author','body','pk']

class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username']

class PostCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    author = serializers.CharField()
    body = serializers.CharField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
