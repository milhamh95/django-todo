from django.shortcuts import render, redirect
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
    
    def post(self, request):
        title = request.POST.get("title")
        content = request.POST.get("content")

        Todo.objects.create(title=title, content=content, user=request.user)

        return redirect("index_view")