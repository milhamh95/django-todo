from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo
from .tasks import todo_archived

# Create your views here.
class TodoListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Todo
    template_name = 'list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user, is_done=False)

class TodoDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Todo
    template_name = 'detail.html'
    context_object_name = 'todo'
    pk_url_kwarg = 'id'


class TodoCreateView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, 'create.html')

    def post(self, request):
        title = request.POST.get('title').strip()
        description = request.POST.get('description')

        if not title:
            return render(request, 'create.html', {'error': 'Title is required'})

        if len(title) > 255:
            return render(request, 'create.html', {'error': 'Title is too long'})

        Todo.objects.create(
            title=title,
            description=description,
            user=request.user,
            status=Todo.Status.ACTIVE
        )

        return redirect('todo_list')

class TodoUpdateView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, id):
        todo = Todo.objects.get(id=id)
        return render(request, 'update.html', {'todo': todo})

    def post(self, request, id):
        todo = Todo.objects.get(id=id)
        title = request.POST.get('title').strip()
        description = request.POST.get('description')

        if not title:
            return render(request, 'update.html', {
                'todo': todo,
                'error': 'Title is required'
            })

        if len(title) > 255:
            return render(request, 'update.html', {
                'todo': todo,
                'error': 'Title is too long'
            })

        todo.title = title
        todo.description = description
        todo.save()

        return redirect('todo_list')

class TodoCompleteView(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request, id):
        todo = Todo.objects.get(id=id)
        todo.is_done = True
        todo.save()

        todo_archived(id)

        return redirect('todo_list')

class TodoDeleteView(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request, id):
        Todo.objects.get(id=id).delete()

        return redirect('todo_list')
