from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        ('todo', 'ToDo'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES)
    due_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title