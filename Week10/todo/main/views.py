from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import List, tdManager
from .forms import ListForm
from django.contrib import messages
from django.views.generic import CreateView, ListView, DeleteView, View
from django.urls import reverse_lazy

class TaskListView(ListView):
	model = List
	context_object_name = 'tasks'

class CompTaskListView(ListView):
	model = List
	context_object_name = 'tasks'
	template_name_suffix = 'listcomp_list'

class CreateTask(CreateView):
	model = List
	success_url = reverse_lazy('list_list')
	fields = ["name", "due"]


class DeleteTaskView(DeleteView):
	model = List
	success_url = reverse_lazy('list_list')

	def get_queryset(self):
		return List.objects.for_user(user=self.request.user)

class Done_task(View):
	def get(self,request,list_id):
		item = List.objects.get(pk=list_id)
		if item.status:
			item.status = False
		else:
			item.status = True
		item.save()
		return redirect('list_list')

class Not_done_task(View):
	def get(self,request,list_id):
		item = List.objects.get(pk=list_id)
		if item.status:
			item.status = False
		else:
			item.status = True
		item.save()
		return redirect('listcomp_list')


