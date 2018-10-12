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
	tasks = List.objects.all
	return render(request, 'completed_todo_list.html', {'tasks': tasks})

def delete_list(request):
	List.objects.all().delete()
	return redirect('todo_list')

def task_done(request,list_id):
	item = List.objects.get(pk=list_id)
	if item.status:
		item.status = False
	else:
		item.status = True

	item.save()
	
	return redirect('todo_list')

def task_notdone(request, list_id):
	item = List.objects.get(pk=list_id)
	if item.status:
		item.status = False
	else:
		item.status = True

	item.save()
	
	return redirect('completed_todo_list')

def delete_task(request,list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	return redirect('todo_list')

def edit_task(request, list_id):
    item = List.objects.get(pk=list_id)

    if request.method == "POST":
        form = ListForm(request.POST,instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('todo_list')
    else:
        form = ListForm(instance=item)

    return render(request, 'edit_task.html', {'form': form})


