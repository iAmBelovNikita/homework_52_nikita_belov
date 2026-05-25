from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import TodoTask, status_choices


# Create your views here.

def todo_list(request):
    tasks = TodoTask.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', {'status_choices': status_choices})
    elif request.method == 'POST':
        TodoTask.objects.create(
            description = request.POST.get('description'),
            status = request.POST.get('status'),
            finish_date = request.POST.get('finish_date') or None
        )
        return HttpResponseRedirect('/')

def task_delete(request):
    if request.method == 'GET':
        task_id = request.GET.get('id')
        TodoTask.objects.filter(id=task_id).delete()
        return HttpResponseRedirect('/')