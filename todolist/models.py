from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    title =models.CharField(max_length=200)
    description =models.TextField(max_length=500)
    status =models.CharField(max_length=10, choices=(('YES','completed'),('Not','Not completed')))


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['status']
