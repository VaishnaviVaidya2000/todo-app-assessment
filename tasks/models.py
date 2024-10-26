from django.db import models

# Create your models here.


class Task(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing integer ID
    task = models.CharField(max_length=255)  # Task description
    completed = models.BooleanField(default=False)  # Task completion status

    def __str__(self):
        return f"{self.task} - {'Completed' if self.completed else 'Pending'}"

