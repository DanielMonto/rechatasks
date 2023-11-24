from django.shortcuts import render,redirect
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest
from .models import Task, SubTask
from django.views import View

class TasksView(View): 
    def get(self, request:HttpRequest):
        if isinstance(request.user,AnonymousUser):
            return redirect('login')
        else:
            tasks = Task.objects.filter(user=request.user, important=False)
            return render(request, 'tasks/tasks.html', {'tasks': tasks})

    def post(self, request:HttpRequest):
        if isinstance(request.user,AnonymousUser):
            return redirect('login')
        else:
            data = request.POST
            taskname = data['name']
            try:
                task = Task.objects.get(name=taskname, user=request.user)
                if data['forcomplete']:
                    task.completed = bool(data['completed'])
                elif data['forimportant']:
                    task.important = bool(data['important'])
                else:
                    task.name = taskname
                    task.important = bool(data['important'])
                    task.completed = bool(data['completed'])
                    task.description = bool(data['description'])
                task.save()
                return redirect('tasks')
            except:
                return redirect('taskswitherror', error=f'la tarea {taskname} no existe')

    def delete(self, request:HttpRequest):
        if isinstance(request.user,AnonymousUser):
            return redirect('login')
        else:
            data = request.POST
            taskname = data['name']
            try:
                task = Task.objects.get(user=request.user, name=taskname)
                task.delete()
                return redirect('tasks')
            except:
                return redirect('taskswitherror', error=f'la tarea {taskname} no existe')
    
class CreateTaskView(View):
    def get(self,request:HttpRequest):
        if isinstance(request.user,AnonymousUser):
            return redirect('login')
        else:
            return render(request,'tasks/createtask.html')
    def post(self,request:HttpRequest):
        if isinstance(request.user,AnonymousUser):
            return redirect('login')
        else:
            data=request.POST
            taskname=data['name']
            tasks=Task.objects.filter(name=taskname,user=request.user)
            if len(tasks)!=0:
                return redirect('createtaskwitherror',error=f'el nombre {taskname} esta en uso')
            else:
                task=Task(
                            name=taskname,
                            description=data['description'],
                            user=request.user
                        )
                task.save()
                return redirect('tasks')
        
def createtaskwitherror(request:HttpRequest,error):
    if isinstance(request.user,AnonymousUser):
        return redirect('login')
    else:
        return render(request,'tasks/createtask.html',{'error':error})        

def taskswitherror(request:HttpRequest,error):
    if isinstance(request.user,AnonymousUser):
        return redirect('login')
    else:
        tasks=Task.objects.filter(user=request.user,important=False)
        return render(request,'tasks/tasks.html',{'error':error,'tasks':tasks})

### SUBTASKS ###
class SubtasksView(View):
    def get(self,request:HttpRequest,taskname):
        if isinstance(request.user,AnonymousUser):
            return redirect('login')
        else:
            try:
                task=Task.objects.get(name=taskname,user=request.user)
                subtasks=SubTask.objects.filter(task=task,important=False)
                return render(request,'tasks/subtasks.html',{'subtasks':subtasks})
            except:
                return redirect('subtaskswitherror',error=f'la tarea {taskname} no existe')
    def post(self,request:HttpRequest,taskname):
        if isinstance(request.user,AnonymousUser):
            return redirect('login')
        else:
            data=request.POST
            subtaskname=data['name']
            try:
                taskm=Task.objects.get(name=taskname,user=request.user)
                try:
                    subtask=SubTask.objects.get(name=subtaskname,task=taskm)
                    if data['forcomplete']:
                        subtask.completed=bool(data['completed'])
                    elif data['forimportant']:
                        subtask.important=bool(data['important'])
                    else:
                        subtask.name=subtaskname
                        subtask.important=bool(data['important'])
                        subtask.completed=bool(data['completed'])
                        subtask.description=data['description']
                    subtask.save()
                    return redirect('subtasks',taskname=taskname)
                except:
                    return redirect('subtaskswitherror',error=f'la minitarea {subtaskname} no existe')
            except:
                return redirect('taskswitherror',error=f'la tarea {taskname} no existe')
        
    def delete(self,request:HttpRequest,taskname):
        if isinstance(request.user,AnonymousUser):
            return redirect('login')
        else:
            data=request.POST
            subtaskname=data['name']
            try:
                taskm=Task.objects.get(name=taskname,user=request.user)
                try:
                    subtask=SubTask.objects.get(name=subtaskname,task=taskm,user=request.user)
                    subtask.delete()
                    return redirect('subtasks',taskname=taskname)
                except:
                    return redirect('subtaskswitherror',taskname=taskname,error=f'la minitarea {subtaskname} no existe')
            except:
                return redirect('taskswitherror',error=f'la tarea {taskname} no existe')
        
class CreateSubTaskView(View):
    def get(self,request:HttpRequest,taskname):
        if isinstance(request.user,AnonymousUser):
            return redirect('login')
        else:
            return render(request,'tasks/createsubtask.html',{'taskname':taskname})
    def post(self,request:HttpRequest,taskname):
        if isinstance(request.user,AnonymousUser):
            return redirect('login')
        else:
            data=request.POST
            subtaskname=data['name']
            try:
                task=Task.objects.get(name=taskname)
                try:
                    subtask=SubTask(
                            name=subtaskname,
                            description=bool(data['description']),
                            important=bool(data['important']),
                            task=task
                        )
                    subtask.save()
                    return redirect('subtasks',taskname=taskname)
                except:
                    return redirect('createsubtaskwitherror',taskname=taskname,error=f'el nombre {subtaskname} esta en uso')
            except:
                return redirect('createsubtaskwitherror',taskname=taskname,error=f'la tarea {taskname} no existe')
    
def subtaskswitherror(request:HttpRequest,taskname,error):
    if isinstance(request.user,AnonymousUser):
        return redirect('login')
    else:
        try:
            task=Task.objects.get(name=taskname,important=False)
            subtasks=SubTask.objects.filter(task=task)
            return render(request,'tasks/subtasks.html',subtasks=subtasks,error=error)
        except:
            return redirect('taskswitherror',error=f'la tarea {taskname} no existe')
    
def createsubtaskwitherror(request:HttpRequest,taskname,error):
    if isinstance(request.user,AnonymousUser):
        return redirect('login')
    else:
        return render(request,'tasks/createsubtask.html',{'taskname':taskname,'error':error})