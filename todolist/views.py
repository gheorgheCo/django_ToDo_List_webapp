from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class Login(LoginView):
    template_name='todolist/login.html'
    fields='__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
class Register(FormView):
    template_name='todolist/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('tasks')

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(Register,self).form_valid(form)


class Tasklist(LoginRequiredMixin,ListView):
    model = Task

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['object_list']=context['object_list'].filter(user=self.request.user)
        context['count']=context['object_list'].filter(status=False).count()
        return context



class CreateTask(LoginRequiredMixin,CreateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(CreateTask,self).form_valid(form)

class UpdateTask(LoginRequiredMixin,UpdateView):
    model =Task
    fields=['title','status','description']
    success_url=reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(UpdateTask,self).form_valid(form)


class DeleteTask(LoginRequiredMixin,DeleteView):
    model =Task
    fields='__all__'
    success_url=reverse_lazy('tasks')

def logoutUser(request):
    logout(request)
    return redirect('login')