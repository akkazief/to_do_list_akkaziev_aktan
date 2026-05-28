from django.shortcuts import render, redirect, reverse

from tasks.models import Task
from tasks.forms import TaskForm


def tasks(request):
    tasks = Task.objects.all()
    context = {'tasks.json': tasks}
    return render(request, 'tasks.html', context)

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')