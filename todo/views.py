from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from django.shortcuts import render

from todo.models import Todo


def index(request):
    return render(request, "base.html")


class TodoListView(ListView):
    model = Todo
    template_name = "todo_list.html"
