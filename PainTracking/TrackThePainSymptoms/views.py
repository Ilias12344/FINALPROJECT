from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout

def login(request):
    return render(request, 'login.html')


def HomePage(request):
    return render(request, 'HomePage.html')  # Make sure this template exists!


def signup(request):
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request, 'dashboard.html')