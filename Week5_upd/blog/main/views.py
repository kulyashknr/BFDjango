from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm, CommentForm
from django.utils import timezone

# Create your views here.
def home(request):
	posts = Blog.objects.filter(create__lte=timezone.now()).order_by('-create')
	return render(request, 'home.html', {'posts': posts})

def index(request):
	if request.method == 'POST':
		form = BlogForm(request.POST or None)

		if form.is_valid():
			form.save()
			posts = Blog.objects.all
			return render(request,'index.html',{'posts': posts})

	else:
		
		posts = Blog.objects.all
		return render(request, 'index.html', {'posts': posts})

def info(request, pk):
    post = Blog.objects.get(pk=pk)
    return render(request, 'info.html', {'post': post})

def deleted(request, pk):
    post = Blog.objects.get(pk=pk)
    post.delete()
    return redirect('home')

def edit(request, pk):
    post = Blog.objects.get(pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('info', pk=post.pk)
    else:
        form = BlogForm(instance=post)
    return render(request, 'edit.html', {'form': form})

def add_comment(request, pk):
    post = Blog.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('info', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})