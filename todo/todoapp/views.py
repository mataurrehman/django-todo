"""
View for my todo
"""
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from .models import TodoItem
# Create your views here.

def home(request):
    """
    List of all todo items
    """
    todo_list = TodoItem.objects.filter(author=request.user.id)
    return render(request, 'todoapp/home.html', {'todo_list':todo_list})
