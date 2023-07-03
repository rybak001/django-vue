from django.db.models import Q
from django.shortcuts import Http404
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializer import PostSerializer

class PostViewList(APIView):

    def get(self, request, format=None):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
class PostDetailedView(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk) 
        except Post.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
@api_view(['POST'])
def search (request):
    query = request.data.get('query','')

    if query:
        posts= Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    else:
        return Response({"posts": []})
    
@api_view(['DELETE'])
def delete(request, pk):

    if Post.objects.get(pk=pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return JsonResponse({'message': 'Delete successful'})
    else:
        return JsonResponse({'message': 'Delete failed'})