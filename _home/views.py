from django.shortcuts import render

# Create your views here
def _home(request):
        
    return render(request, 'home.html')
