from django.urls import path
from main import views
from . import views

urlpatterns = [
    path('', views.todo_list, name="todo_list"),
    path('completed_todo_list/', views.completed_todo_list, name="completed_todo_list"),
    path('delete_list', views.delete_list, name="delete_list"),
]