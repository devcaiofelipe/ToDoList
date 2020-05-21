from django.urls import path
from .views import TasksList, TaskDetail, TaskInsert, TaskEdit, TaskDelete, TaskStatusChance

urlpatterns = [
    path('', TasksList, name='TasksList'),
    path('task/<int:id>', TaskDetail, name='TaskDetail'),
    path('newtask/', TaskInsert, name='TaskInsert'),
    path('edit/<int:id>', TaskEdit, name='TaskEdit'),
    path('changestatus/<int:id>', TaskStatusChance, name='TaskStatusChance'),
    path('delete/<int:id>', TaskDelete, name='TaskDelete'),
]
