from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Pack, Premium

def home(request):
    return render(request, 'home/index.html')