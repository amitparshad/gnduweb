from django.db import models
from events.models import event
class student(models.Model):
    event=models.ManyToManyField(event)
    username=models.CharField( max_length=30,)
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=40)
    def __str__(self):
        return self.username
