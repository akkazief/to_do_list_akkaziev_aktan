from django.shortcuts import render, redirect,get_object_or_404, reverse

from tasks.models import Task
from tasks.forms import TaskForm


def tasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/tasks.html', context)


def details(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, "tasks/details.html", context)


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

def task_update(request, pk, *args, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task)
    context = {'form': form}

    if request.method == 'GET':
        return render(request, 'tasks/task_update.html', context)   #добавить#
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("detail", pk=task.pk)
        return render(request, 'tasks/task_update.html', {'form': form})


def delete_task(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.delete()
    return redirect('main')
