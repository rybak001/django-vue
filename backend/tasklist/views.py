from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializer import PostSerializer

class PostViewList(APIView):

    def get(self, request, format=None):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)