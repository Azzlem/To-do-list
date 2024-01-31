from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from django.shortcuts import render

from todo.forms import TodoForm
from todo.models import Todo


def index(request):
    return render(request, "todo/base.html")


class TodoListView(ListView):
    model = Todo
    template_name = "todo/todo_list.html"


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/todo_form.html"

    def get_success_url(self):
        return reverse('todo:todo_list')


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/todo_update_form.html"

    def get_form(self, form_class=None):
        form = super(TodoUpdateView, self).get_form(form_class)
        return form

    def get_success_url(self):
        return reverse('todo:todo_list')
