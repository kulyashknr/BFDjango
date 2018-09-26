from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import List

from .forms import ListForm

from django.contrib import messages

def todo_list(request):
    if request.method == 'POST':
    	form = ListForm(request.POST or None)

    	if form.is_valid():
    		form.save()
    		tasks = List.objects.all
    		return render(request,'todo_list.html',{'tasks': tasks})

    else:
    	tasks = List.objects.all
    	return render(request, 'todo_list.html', {'tasks': tasks})


def completed_todo_list(request):

	context = {
	'num': [i for i in range(1, 2)],
	'created': datetime.now(),
	'status': True,
	'owner': "admin",
	'due_on': datetime(2018, 9, 27)
	}

	return render(request, 'completed_todo_list.html', context)

def delete_list(request):
    List.objects.all().delete()
    return redirect('todo_list')

