from django.conf.urls import url
from django.urls import path, include
from .views import AddTodo, DeleteTodo

app_name = 'todo'

urlpatterns = [
    url(r'^add/', AddTodo, name='add'),
    url(r'^delete/(?P<todo_id>\d+)/', DeleteTodo, name='delete'),
]
