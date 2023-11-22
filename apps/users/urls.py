from django.urls import path
from . import views

urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('singup/',views.SignUpView.as_view(),name='signup'), 
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('delete/',views.DeleteUserView.as_view(),name='deleteuser')
] 