from django.db import models

# Create your models here.


class TodoTask(models.Model):
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    date = models.DateField()

