from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import authenticate, login

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        authenticated_user = authenticate(request, username=username, password=password)

        if authenticated_user is None:
            print("Invalid credentials")
            return redirect('login')

        login(request, authenticated_user)
        return redirect('todo_list')

class LogoutView(View):
    def get(self, request):
        return redirect('login')

class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        return redirect('todo_list')
