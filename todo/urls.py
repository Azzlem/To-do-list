from django.urls import path

from todo import views
from todo.apps import TodoConfig
from todo.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoListSuccessView, \
    TodoListUnSuccessView

app_name = TodoConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('todo_list/', TodoListView.as_view(), name='todo_list'),
    path('todo_form/', TodoCreateView.as_view(), name='todo_form'),
    path('todo_update/<int:pk>/', TodoUpdateView.as_view(), name='todo_update'),
    path('todo_delete/<int:pk>/', TodoDeleteView.as_view(), name='todo_delete'),
    path('todo_list_success/', TodoListSuccessView.as_view(), name='todo_list_success'),
    path('todo_list_unsuccess/', TodoListUnSuccessView.as_view(), name='todo_list_unsuccess'),
]
