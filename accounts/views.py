from django.shortcuts import redirect, render
from django.views.generic import View

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, "login.html")
