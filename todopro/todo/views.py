from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.urls import reverse


def index(request):
    tasks = Task.objects.all().order_by ('-created_at')
    return render(request, 'index.html', {'tasks': tasks})

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title').strip()
        description = request.POST.get('description')
        if title:  # Check if title is not empty
            Task.objects.create(title=title, description=description)
            return redirect(reverse('index'))
        error_message = "Title cannot be empty."
        return render(request, 'add.html', {'error_message': error_message})
    return render(request, 'add.html')

def update(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        title = request.POST.get('title').strip()
        description = request.POST.get('description').strip()
        completed = request.POST.get('completed') == 'on'
        if title:  # Check if title is not empty
            task.title = title
            task.description = description
            task.completed = completed
            task.save()
            return redirect(reverse('index'))
        error_message = "Title cannot be empty."
        return render(request, 'update.html', {'task': task, 'error_message': error_message})
    return render(request, 'update.html', {'task': task})
def delete(request, id):
    task = get_object_or_404(Task, id=id)   
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('index'))
    return render(request, 'delete.html', {'task': task})
def toggle(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = not task.completed
    task.save()
    return redirect(reverse('index'))