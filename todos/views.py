from django.views.generic import ListView

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
