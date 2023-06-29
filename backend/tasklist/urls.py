from django.urls import path, include
from .views import PostViewList

urlpatterns = [
    path('posts', PostViewList.as_view())
]