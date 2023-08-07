import django_filters 
from .models import Task

class TaskFilter(django_filters.FilterSet):
    class Meta:
        fields = {
            'title': ['exact', 'icontains'],
            'status': ['exact'],
            'due_date': ['exact', 'gt', 'lt'],
        }