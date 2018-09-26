from django.db import models
from datetime import datetime

class List(models.Model):
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name