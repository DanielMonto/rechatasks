from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect

def mainpoint(request):
    return redirect('home')

urlpatterns = [
    path('',mainpoint),
    path('admin/', admin.site.urls),
    path('messages/',include('apps.messagesrenamed.urls')),
    path('tasks/',include('apps.tasks.urls')),
    path('users/',include('apps.users.urls')),
]
