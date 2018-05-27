from django.db import models
class Student(models.Model):
    Username = models.CharField(max_length=250)
    Password = models.CharField(max_length=250)
