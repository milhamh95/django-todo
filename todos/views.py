from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render

# Create your views here.
class TodoListView(ListView):
    template_name = 'list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return [
            {'id': 1, 'title': 'Learn Django', 'completed': False},
            {'id': 2, 'title': 'Build Todo App', 'completed': True},
            {'id': 3, 'title': 'Write Tests', 'completed': False},
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ini List Todo'
        return context

class TodoDetailView(DetailView):
    template_name = 'detail.html'
    context_object_name = 'todo'

    def get_object(self, queryset=None):
        todo_id = self.kwargs.get('id')
        todos = [
            {'id': '1', 'title': 'Learn Django', 'completed': False},
            {'id': '2', 'title': 'Build Todo App', 'completed': True},
            {'id': '3', 'title': 'Write Tests', 'completed': False},
        ]

        for todo in todos:
            if todo['id'] == todo_id:
                return todo

        return None

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
