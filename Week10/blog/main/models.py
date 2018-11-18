from django.db import models
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class BlogManager(models.Manager):
	def for_user(self, user):
		return self.filter(author=user)

class Blog(models.Model):
	title = models.CharField(max_length=120)
	create = models.DateTimeField(default=datetime.now, blank=True)
	text = models.CharField(max_length=800)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	objects = BlogManager()


	def __str__(self):
		return self.tit_bl + ' | ' + str(self.createted_at) + ' | ' + self.text_bl


	def get_absolute_url(self):
		return reverse_lazy('blog_list')

class Comment(models.Model):
	post = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
	author = models.CharField(max_length=200)
	text = models.TextField()
	created = models.DateTimeField(default=datetime.now)


	def get_absolute_url(self):
		return reverse_lazy('blog_list')


	def __str__(self):
		return self.author + ' | ' + str(self.created) + ' | ' + self.text

