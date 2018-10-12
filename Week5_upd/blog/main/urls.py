from django.urls import path
from main import views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('index/', views.index, name="index"),
    path('post/<int:pk>/', views.info, name='info'),\
    path('post/(?P<pk>\d+)/deleted/$', views.deleted, name='deleted'),
    path('post/<int:pk>/edit/', views.edit, name='edit'),
    path('post/(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
]