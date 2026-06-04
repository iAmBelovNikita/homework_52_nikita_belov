from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoTask
from .forms import TaskForm

# Create your views here.

def todo_list(request):
    tasks = TodoTask.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def task_about(request, pk):
    task = get_object_or_404(TodoTask, pk=pk)
    return render(request, 'task_about.html', {'task': task})

def task_create(request):
    form = TaskForm()

    if request.method == 'GET':
        context = {
            'form': form
        }
        return render(request, 'task_create.html', context)

    elif request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = TodoTask(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                status=form.cleaned_data.get('status'),
                finish_date=form.cleaned_data.get('finish_date'),
            )
            task.save()

            return redirect('task_about', pk=task.pk)

        context = {
            'form': form
        }
        return render(request, 'task_create.html', context)


def task_delete(request, pk):
    if request.method == 'GET':
        task = get_object_or_404(TodoTask, pk=pk)
        task.delete()
        return redirect('todo_list')