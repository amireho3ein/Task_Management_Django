from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from .filters import TaskFilter
from rest_framework import routers


class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_class = TaskFilter
    

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDeleteView():
    pass

class TaskUpdate():
    pass