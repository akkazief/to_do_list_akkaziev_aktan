from django.http import HttpResponseRedirect
from django.shortcuts import render

from tasks.models import Task
from tasks.forms import TaskForm


def tasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks.html', context)

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})