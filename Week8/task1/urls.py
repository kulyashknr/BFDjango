from django.contrib import admin
from django.urls import path, include
from . import views
from .views import home, rest_list, add_rest, delete_rest, dish_list

urlpatterns = [
	path('', home.as_view(), name='home'),
	path('<int:pk>/', rest_list.as_view()),
	path('add/', add_rest.as_view(), name="add_rest"),
	path('<int:fk>/delete/<int:pk>/', delete_rest.as_view()),
	path('<int:fk>/dishes/<int:pk>/', dish_list.as_view()),
]