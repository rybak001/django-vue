from django.urls import path, include
from .views import PostViewList, PostDetailedView, search

urlpatterns = [
    path('posts', PostViewList.as_view()),
    path('posts/search/', search),
    path('posts/<int:pk>', PostDetailedView.as_view()),
]