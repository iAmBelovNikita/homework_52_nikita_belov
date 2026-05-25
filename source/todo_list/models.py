from django.db import models

# Create your models here.

status_choices = [
    ('new', 'New'),
    ('in_progress', 'In progress'),
    ('done', 'Done'),
]

class TodoTask(models.Model):
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=status_choices, default='new')
    finish_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        db_table = "TodoTask"
        verbose_name = "Task"