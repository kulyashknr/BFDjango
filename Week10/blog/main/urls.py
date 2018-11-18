from django.urls import path
from main import views
from . import views
from .views import PostList, PostCreate, PostDelete, PostDetail, PostUpdate, CommentCreate, CommentList, CommentDelete, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/posted/', PostCreate.as_view(), name='blog_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='blog_detail'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='blog_delete'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='blog_update'),
    path('post/create/', PostCreate.as_view(), name='blog_create'),
    path('comment/<int:pk>/', CommentCreate.as_view(), name='comment_create'),
    path('comment/list/', CommentList.as_view(), name='comment_list'),
    path('comment/<int:pk>/delete/', CommentDelete.as_view(), name='comment_delete'),
]