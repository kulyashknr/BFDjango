from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def todo_list(request):

	context = {
	'num': [i for i in range(1, 5)],
	'created': datetime.now(),
	'status': False,
	'owner': "admin",
	'due_on': datetime(2018, 9, 27)
	}

	return render(request, 'todo_list.html', context)

def completed_todo_list(request):

	context = {
	'num': [i for i in range(1, 2)],
	'created': datetime.now(),
	'status': True,
	'owner': "admin",
	'due_on': datetime(2018, 9, 27)
	}

	return render(request, 'completed_todo_list.html', context)


