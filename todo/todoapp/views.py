"""
View for my todo
"""
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
# Create your views here.

def home(request):
    """
    List of all todo items
    """
    todo_list = TodoItem.objects.filter(author=request.user.id)
    return render(request, 'todoapp/home.html', {'todo_list':todo_list})

def AddTodo(request):
    item = TodoItem(title=request.POST['title'], author=request.user)
    item.save()
    return HttpResponseRedirect('/')

def DeleteTodo(request, todo_id):
    item = get_object_or_404(TodoItem, pk=todo_id)
    item.delete()
    return HttpResponseRedirect('/')
