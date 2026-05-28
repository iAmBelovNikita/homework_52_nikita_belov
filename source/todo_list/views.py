from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import TodoTask, status_choices


# Create your views here.

def todo_list(request):
    tasks = TodoTask.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def task_about(request, pk):
    task = get_object_or_404(TodoTask, pk=pk)
    return render(request, 'task_about.html', {'task': task})

def task_create(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', {'status_choices': status_choices})
    elif request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        status = request.POST.get('status')
        finish_date = request.POST.get('finish_date') or None

        if not title:
            return render(request, 'task_create.html', {'status_choices': status_choices, 'error': 'Title cannot be empty'})

        TodoTask.objects.create(
            title = title,
            description = description,
            status = status,
            finish_date = finish_date
        )

        return HttpResponseRedirect('/')

def task_delete(request):
    if request.method == 'GET':
        task_id = request.GET.get('id')
        TodoTask.objects.filter(id=task_id).delete()
        return HttpResponseRedirect('/')