from django.urls import path

from todo import views
from todo.apps import TodoConfig
from todo.views import TodoListView

app_name = TodoConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('todo_list/', TodoListView.as_view(), name='todo_list'),

]
