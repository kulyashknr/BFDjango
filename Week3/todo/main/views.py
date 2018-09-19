from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def todo_list(request):

	context = {
	'numbers': [i for i in range(0, 5)],
	'created': datetime.now(),
	'status': False,
	'owner': "Admin",
	'due_on': datetime(2018, 9, 9)
	}

	return render(request, 'todo_list.html', context)

def completed_todo_list(request):

	context = {
	'numbers': [i for i in range(0, 3)],
	'created': datetime.now(),
	'status': True,
	'owner': "Admin",
	'due_on': datetime(2018, 9, 9)
	}

	return render(request, 'completed_todo_list.html', context)


