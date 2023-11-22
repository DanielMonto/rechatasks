from django.urls import path
from . import views

urlpatterns=[
    path('',views.TasksView.as_view(),name='tasks'),
    path('<str:error>/',views.taskswitherror,name='taskswitherror'),
    path('create/',views.CreateTaskView.as_view(),name='createtask'),
    path('create/<str:error>/',views.createtaskwitherror,name='createtaskwitherror'),
]