from django.shortcuts import render
from services.models import Services

# Create your views here.
def home_screen_view(request, *args, **kwargs):
    context = {}

    services = Services.objects.all()
    context['services'] = services
    
    return render(request, "home/index.html", context)