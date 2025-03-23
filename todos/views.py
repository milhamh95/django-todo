from django.shortcuts import render
from django.views import View
from .models import Todo

# Create your views here.
class IndexView(View):
    def get(self, request):
        todos = Todo.objects.all()
        context = {
            "todos": todos,
        }
        return render(request, "index.html", context)