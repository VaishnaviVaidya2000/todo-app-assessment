from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# View to display all tasks
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list_tasks.html', {'tasks': tasks})

# View to add a new task
def add_task(request):
    if request.method == "POST":
        task_name = request.POST['task']
        Task.objects.create(task=task_name, completed=False)
        return redirect('list_tasks')
    return render(request, 'tasks/add_task.html')

# View to delete a task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('list_tasks')

# View to mark a task as completed
def mark_task_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('list_tasks')

