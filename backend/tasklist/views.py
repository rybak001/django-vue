from django.db.models import Q
from django.shortcuts import Http404
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token

from .models import Post, User
from .serializer import PostSerializer, UserSerializer, PostCreateSerializer

class UserViewList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


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
    
@login_required
def logout(self, request):
    # Get the user's token
    token = request.auth

    # Delete the token to log the user out
    token.delete()

    return Response({"detail": "Successfully logged out."})

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
    
@api_view(['POST'])
@login_required
@permission_required('tasklist.add_post')
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Exclude 'author' field from the request data
    request_data = request.data.copy()
    request_data.pop('author', None)

    serializer = PostCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)

@api_view(['POST'])
@login_required
@permission_required('tasklist.add_post')
def add_post(request):
    serializer = PostCreateSerializer(data=request.data)
    if serializer.is_valid():
        post = serializer.save(author=request.user)  # Set the author as the current user
        return Response(PostSerializer(post).data, status=201)
    return Response(serializer.errors, status=400)
    
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Authenticate user
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # Log the user in
        login(request, user)

        # Generate or retrieve the token for the user
        token, _ = Token.objects.get_or_create(user=user)

        return Response({'auth_token': token.key})
    else:
        return Response({'error': 'Invalid credentials'}, status=400)
    
