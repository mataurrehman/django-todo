from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class TodoItem(models.Model):
    title = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'TODOs'
        verbose_name_plural = 'TODOs'
