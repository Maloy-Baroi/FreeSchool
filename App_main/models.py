from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Routine(models.Model):
    Department = models.CharField(max_length=120)
    Batch = models.CharField(max_length=30)
    Section = models.CharField(max_length=30)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Routine_Author')
    Routine_image = models.ImageField(upload_to='Routine', default='/static/image/defaultRoutine.jpg')
    Publish_date = models.DateTimeField(auto_now_add=True)


class ClassVideo(models.Model):
    Video_title = models.CharField(max_length=256)
    Department = models.CharField(max_length=120)
    Batch = models.CharField(max_length=30)
    Section = models.CharField(max_length=30)
    Teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Class_Teacher')
    Video = models.FileField(upload_to='Videos')
    Publish_date = models.DateTimeField(auto_now_add=True)
