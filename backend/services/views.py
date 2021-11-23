from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Competences, Stacks, Experts, Tarifs, Services

def services(request):
    return render(request, 'services/index.html')

def experts(request):
    experts = Experts.objects.all()    
    return render(request, 'experts/index.html', {'experts':experts})