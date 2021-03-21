from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from account.forms import LoginForm

# Create your views here.
def login_view(request, *args, **kwargs):
    context = {}

    user = request.user
    if user.is_authenticated: 
        return redirect("home")

    if request.POST:
        print("success1")
        form = LoginForm(request.POST)
        if form.is_valid():
            print("success2")
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                print("success3")
                login(request, user)
                return redirect("home")

    else:
        print("failed")
        form = LoginForm()

    context['login_form'] = form

    return render(request, "account/login.html", context)
