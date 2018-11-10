from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class tdManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)

class List(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    create = models.DateTimeField(default=datetime.now, blank=True)
    due = models.DateField('Date', blank=True, null=True)
    objects = tdManager()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + ' | ' + str(self.create) + ' | ' + str(self.status) + ' | ' + str(self.due)


