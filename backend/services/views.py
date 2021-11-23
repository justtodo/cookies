from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

from .models import Competences, Stacks, Experts, Tarifs, Services

def services(request):
    services = Services.objects.all()
    return render(request, 'services/index.html', {'services':services})

def experts(request):
    experts = Experts.objects.all()    
    return render(request, 'experts/index.html', {'experts':experts})

def details(request, slug):
    services = get_object_or_404(Services, slug=slug)
    return render(request, 'services/services_page.html', {'services':services})