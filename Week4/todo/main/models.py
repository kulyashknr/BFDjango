from django.db import models
from datetime import datetime

class List(models.Model):
	name = models.CharField(max_length=200)
	create = models.DateTimeField(default=datetime.now, blank=True)
	due = models.DateField('Date', blank=True, null=True)
	
	def __str__(self):
		return self.name + ' | ' + str(self.create) +' | ' + str(self.due)