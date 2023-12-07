from django.urls import path
from .views import Tasklist,CreateTask,UpdateTask,DeleteTask,Login,Register
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
    path('', Tasklist.as_view(),name='tasks'), 
    path('create/',CreateTask.as_view(),name='create-task'),
    path('update/<int:pk>',UpdateTask.as_view(),name='update-task'),
    path('delete/<int:pk>',DeleteTask.as_view(),name='delete-task'),
    path('login/',Login.as_view(), name='login'),
    path('logout/',views.logoutUser,name='logout'),
    #path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',Register.as_view(), name='register'),
]