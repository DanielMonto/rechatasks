from django.urls import path
from . import views

urlpatterns=[
    path('',views.TasksView.as_view(),name='tasks'),
    path('twe/<str:error>/',views.taskswitherror,name='taskswitherror'),
    path('createtask/',views.CreateTaskView.as_view(),name='createtask'),
    path('subtaskswt/<str:taskname>/',views.SubtasksView.as_view(),name='subtasks'),
    path('create/<str:error>/',views.createtaskwitherror,name='createtaskwitherror'),
    path('subtaskswe/<str:taskname>/<str:error>/',views.subtaskswitherror,name='subtaskswitherror'),
    path('subtasksc/create/<str:taskname>/',views.CreateSubTaskView.as_view(),name='createsubtask'),
    path('subtasks/create/<str:taskname>/<str:error>/',views.createsubtaskwitherror,name='createsubtaskwitherror')
]