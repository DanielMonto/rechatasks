from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login,logout 
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render,redirect
from django.views import View

class HomeView(View):
    def get(self,request:HttpRequest): 
        return render(request,'home.html',{'user':request.user})

class SignUpView(View):
    def get(self,request:HttpRequest): 
        return render(request,'users/signup.html')
    def post(self,request:HttpRequest):
        if request.POST['password']==request.POST['repassword']:
            try:
                user=User(username=request.POST['username'],password=make_password(request.POST['password']))
                user.save()
                login(request,user)
                return redirect('tasks')
            except:
                return render(request,'users/signup.html',{'error':'el nombre de usuario esta en uso'})
        else:
            return render(request,'users/signup.html',{'error':'contraseñas no son iguales'})

class LoginView(View):
    def get(self,request:HttpRequest):
        return render(request,'users/login.html')
    def post(self,request:HttpRequest):
        try:
            user=User.objects.get(username=request.POST['username'])
            if make_password(request.POST['password'])==user.password:
                login(request,user)
                return redirect('tasks')
            else:
                return render(request,'user/login.html',{'error':'contraseña incorrecta'})
        except:
            return render(request,'user/login.html',{'error':'usuario no existe'})

class LogoutView(View):
    @login_required
    def get(self,request:HttpRequest):
        logout(request)
        return redirect('home')

class DeleteUserView(View):
    @login_required
    def get(self,request:HttpRequest):
        logout(request)
        request.user.delete()
        return redirect('home')