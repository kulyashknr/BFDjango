from django.urls import path
from main import views
from . import views

urlpatterns = [
    path('', views.todo_list, name="todo_list"),
    path('completed_todo_list/', views.completed_todo_list, name="completed_todo_list"),
    path('delete_list', views.delete_list, name="delete_list"),
    path('task_done/<list_id>', views.task_done, name="task_done"),
    path('task_notdone/<list_id>', views.task_notdone, name="task_notdone"),
    path('delete_task/<list_id>', views.delete_task, name="delete_task"),
]