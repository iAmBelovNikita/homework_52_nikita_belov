from django.urls import path

from .views import todo_list, task_create, task_delete

urlpatterns = [
    path("", todo_list, name="todo_list"),
    path('task/create/', task_create, name='task_create'),
    path('task/delete/', task_delete, name='task_delete'),
]
