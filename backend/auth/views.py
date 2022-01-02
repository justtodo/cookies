from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'auth/login.html')

def signup(request):
    return render(request, 'auth/signup.html')