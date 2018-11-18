from django.urls import path
from . import views
from .views import CreateTask, CompTaskListView, DeleteTaskView, TaskListView, Done_task, Not_done_task

urlpatterns = [
    path('', TaskListView.as_view(), name="list_list"),
    path('completed_todo_list/', CompTaskListView.as_view(), name="listcomp_list"),
    path('<int:pk>/delete/', DeleteTaskView.as_view(), name="list_delete"),
    #path('delete_task/<list_id>', DeleteTaskView.as_view(), name="delete_task"),
    path('create_task/', CreateTask.as_view(), name="create_task"),
    path('<list_id>/done_task/', Done_task.as_view(), name="done_task"),
    path('<list_id>/not_done_task/', Not_done_task.as_view(), name="not_done_task"),
]