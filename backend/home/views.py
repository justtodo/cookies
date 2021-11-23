from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Premium, Packs
from services.models import Services

def home(request):
    premium = Premium.objects.all()
    services = Services.objects.filter(favoris=True)
    return render(request, 'home/index.html', {'premium':premium, 'services':services})