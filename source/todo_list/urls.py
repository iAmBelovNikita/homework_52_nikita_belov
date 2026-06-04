from django.urls import path

from .views import todo_list, task_create, task_delete, task_about, task_update

urlpatterns = [
    path("", todo_list, name="todo_list"),
    path('task/create/', task_create, name='task_create'),
    path('task/update/<int:pk>/', task_update, name='task_update'),
    path('task/delete/<int:pk>/', task_delete, name='task_delete'),
    path('task/<int:pk>/', task_about, name='task_about'),
]
