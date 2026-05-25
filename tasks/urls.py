from django.urls import path
from tasks.views import tasks, create_task, delete_task

urlpatterns = [
    path('', tasks, name='index'),
    path('create_task/', create_task, name='create_task'),
    path('tasks.json/delete_task/<int:pk>/', delete_task, name='delete_task'),
]