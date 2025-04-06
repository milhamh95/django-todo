from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from .models import Todo

# Create your views here.
class TodoListView(ListView):
    model = Todo
    template_name = 'list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'detail.html'
    context_object_name = 'todo'
    pk_url_kwarg = 'id'


class TodoCreateView(View):
    def get(self, request):
        return render(request, 'create.html')

    def post(self, request):
        print("create todo")
        return redirect('todo_list')

class TodoUpdateView(View):
    def get(self, request, id):
        return render(request, 'update.html')

    def post(self, request, id):
        print("update todo: ", id)
        return redirect('todo_list')

class TodoDeleteView(View):
    def post(self, request, id):
        print("delete todo: ", id)

        return redirect('todo_list')
