from django.urls import path, include
from .views import PostViewList, PostDetailedView, UserViewList, search, delete, add_post, login_view,logout

urlpatterns = [
    path('posts', PostViewList.as_view()),
    path('posts/search/', search),
    path('posts/add-post/', add_post),
    path('posts/<int:pk>', PostDetailedView.as_view()),
    path('posts/delete/<int:pk>', delete),
    path('userview/', UserViewList.as_view()),
    path('log-in',login_view),
    path('log-out', logout),
]