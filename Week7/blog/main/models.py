from django.db import models
from datetime import datetime

class Blog(models.Model):
	title = models.CharField(max_length=120)
	create = models.DateTimeField(default=datetime.now, blank=True)
	text = models.CharField(max_length=800)
	
	def __str__(self):
		return self.title + ' | ' + str(self.create) + ' | ' + str(self.text) 

class Comment(models.Model):
    post = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.author + ' | ' + str(self.text)