from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Premium, Packs

def home(request):
    premium = Premium.objects.all()
    return render(request, 'home/index.html', {'premium':premium})