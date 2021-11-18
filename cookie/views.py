
from django.shortcuts import render

# Create your views here
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

def cookie(request):
    
    return render(request, './home/index.html')
