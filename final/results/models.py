from django.db import models
class Result(models.Model):
    Marks = models.FloatField()
    ranks = models.IntegerField(blank=True, null=True)
