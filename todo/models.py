import datetime
from django import forms
from django.db import models
from django.utils import timezone

class TodoList(models.Model):
    item = models.CharField(max_length=300)
    visible = models.BooleanField(default=True)
    pub_date = models.DateTimeField('published date and time', auto_now_add=True)

    def __str__(self):
        return self.item
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


