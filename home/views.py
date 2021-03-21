from django.shortcuts import render

# Create your views here.
def home_screen_view(request, *args, **kwargs):
    return render(request, "home/index.html")