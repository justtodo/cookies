from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

from .models import Produit, Images

def store(request):
    produit = Produit.objects.all()
    return render(request, 'store/index.html', {'produit':produit})

def detail(request, slug):
    produit = get_object_or_404(Produit, slug=slug)
    return render(request, 'store/product_page.html', {'produit':produit})