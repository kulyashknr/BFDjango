from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Blog, Comment
from .forms import BlogForm, CommentForm
from django.utils import timezone
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
    http_method_names = ['get']

class PostList(ListView):
    model = Blog
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Blog

class PostDelete(DeleteView, LoginRequiredMixin):
    model = Blog
    success_url = reverse_lazy('blog_list')

    def get_queryset(self):
        return Blog.objects.for_user(user=self.request.user)

class PostUpdate(UpdateView, LoginRequiredMixin):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog_list')
    template_name_suffix = '_update_form'

    def get_queryset(self):
        return Blog.objects.for_user(user=self.request.user)

class PostCreate(CreateView, LoginRequiredMixin):
    model = Blog
    success_url = reverse_lazy('blog_list')
    fields = ["id","title","create","text"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(Blog, self).form_valid(form)

class CommentList(ListView):
    model = Comment
    context_object_name = 'comments'

class CommentCreate(CreateView):
    model = Comment
    fields = ["post","author", "text"]

class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('blog_list')