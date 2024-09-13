from django.shortcuts import render , redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        if task_name:
            new_task = Task(name = task_name)
            new_task.save()
        return redirect('/')
    return render(request , 'index.html', {'tasks' : tasks})

def complete_task(request, task_id):
    task = Task.objects.get(id = task_id)
    task.completed = True
    task.save()
    return redirect('/')

def delete_task(request, task_id):
    task = Task.objects.get(id = task_id)
    task.delete()
    return redirect('/')

    
