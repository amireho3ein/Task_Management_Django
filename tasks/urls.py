from django.urls import path
from .views import TaskListView, TaskDetailView
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('tasks/', views.TaskListView)
router.register('tasks/<int:pk>/', views.TaskDetailView)

                
                
urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]