from django.db import models
class Computer(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=30)
    option2 = models.CharField(max_length=30)
    option3 = models.CharField(max_length=30)
    option4 = models.CharField(max_length=30)
    correct = models.CharField(max_length=30)


class English(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=30)
    option2 = models.CharField(max_length=30)
    option3 = models.CharField(max_length=30)
    option4 = models.CharField(max_length=30)
    correct = models.CharField(max_length=30)


class Math(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=30)
    option2 = models.CharField(max_length=30)
    option3 = models.CharField(max_length=30)
    option4 = models.CharField(max_length=30)
    correct = models.CharField(max_length=30)


class Science(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=30)
    option2 = models.CharField(max_length=30)
    option3 = models.CharField(max_length=30)
    option4 = models.CharField(max_length=30)
    correct = models.CharField(max_length=30)

