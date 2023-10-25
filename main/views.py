from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def index_view(request):
    context={
        'tasks': Todo.objects.all()
    }
    return render(request,'index.html',context)
def create_task_view(request):
    if request.method == "POST":
        task= request.POST['task']
        Todo.objects.create(
            task=task
        )
        return redirect('index_url')
    context={
        'tasks':Todo.objects.all()
    }
    return render(request,'index.html',context)

def delete_task_view(request,pk):
    task= Todo.objects.get(pk = pk)
    task.status = "DELETED"
    task.save()
    return redirect('index_url')

def finished_task_view(request,pk):
    task= Todo.objects.get(pk=pk)
    task.status = "FINISHED"
    task.save()
    return redirect('index_url'),

def finished_view(request):
     task = Todo.objects.filter(status= "FINISHED")
     context={
         'task':task
     }
     return render(request,'Finished.html',context)


def delete_status_view(request):
    task = Todo.objects.filter(status = "DELETED")
    context={
        'task': task
    }
    return render(request,'delete_status.html',context)
def In_progress_view(request):
    task= Todo.objects.filter(status = "In progress")
    context={
        'task':task
    }
    return render(request,'in_progress.html',context)
