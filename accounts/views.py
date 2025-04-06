from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
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
        logout(request)
        return redirect('login')

class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        email = request.POST.get('email').strip()
        first_name = request.POST.get('first_name').strip()
        last_name = request.POST.get('last_name').strip()
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        password2 = request.POST.get('password2').strip()

        if username is None or username == "":
            return render(
                request,
                'register.html',
                {"error": "Username is required"})

        if password is None or password == "":
            return render(
                request,
                'register.html',
                {"error": "Password is required"})

        if password != password2:
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
