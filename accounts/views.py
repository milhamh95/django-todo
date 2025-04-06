from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        authenticated_user = authenticate(request, username=username, password=password)

        if authenticated_user is None:
            return render(
                request,
                'login.html',
                {"error": "Invalid credentials"})

        login(request, authenticated_user)
        return redirect('todo_list')

class LogoutView(View):
    def get(self, request):
        return redirect('login')

class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            print("Passwords do not match")
            return render(
                request,
                'register.html',
                {"error": "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(
                request,
                'register.html',
                {"error": "Username already exists"})

        if User.objects.filter(email=email).exists():
            return render(
                request,
                'register.html',
                {"error": "Email already exists"})

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        login(request, user)
        return redirect('todo_list')
