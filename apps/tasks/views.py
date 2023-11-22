from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Task, SubTask
from django.views import View

class TasksView(View):
    @login_required
    def get(self,request:HttpRequest):
        tasks=Task.objects.filter(user=request.user,important=False)
        return render(request,'tasks/tasks.html',{'tasks':tasks})
    @login_required
    def put(self,request:HttpRequest):
        data=request.POST
        try:
            task=Task.objects.get(id=data['id'])
            if data['forcomplete']:
                task.completed=data['completed']
            elif data['forimportant']:
                task.important=data['important']
            else:
                task.name=data['name']
                task.important=data['important']
                task.completed=data['completed']
                task.description=data['description']
            task.save()
            return redirect('tasks')
        except:
            return redirect('taskswitherror',error=f'la tarea {task.name} no existe')
    @login_required
    def delete(self,request:HttpRequest):
        data=request.POST
        try:
            task=Task.objects.get(id=data['id'])
            task.delete()
            return redirect('tasks')
        except:
            return redirect('taskswitherror',error=f'la tarea {task.name} no existe')
    
class CreateTaskView(View):
    @login_required
    def get(self,request:HttpRequest):
        return render(request,'createtask.html')
    @login_required
    def post(self,request:HttpRequest):
        data=request.POST
        try:
            task=Task(
                        name=data['name'],
                        description=data['description'],
                        important=data['important'],
                        user=request.user
                    )
            task.save()
            return redirect('tasks')
        except:
            return redirect('createtaskwitherror',error='nombre de tarea en uso')
  
@login_required      
def createtaskwitherror(request:HttpRequest,error):
    return render(request,'createtask.html',{'error':error})        

@login_required
def taskswitherror(request:HttpRequest,error):
    tasks=Task.objects.filter(user=request.user)
    return render(request,'tasks/tasks.html',{'error':error,'tasks':tasks})