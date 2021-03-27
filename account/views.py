from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from account.forms import LoginForm, UserChangeForm, UserCreationForm

# Create your views here.
def login_view(request, *args, **kwargs):
    context = {}

    user = request.user
    if user.is_authenticated: 
        if user.is_staff:
            return redirect("appointment:list")                
        else:
            return redirect("appointment:add")

    if request.POST:
        print("success1")
        form = LoginForm(request.POST)
        if form.is_valid():
            print("success2")
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                if user.is_staff:
                    return redirect("appointment:list")                
                else:
                    return redirect("appointment:add")

    else:
        print("failed")
        form = LoginForm()

    context['login_form'] = form

    return render(request, "account/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')

def registration_view(request):
    context = {}

    if request.POST:
        form = UserCreationForm(request.POST)
        print('success1')

        if form.is_valid():
            print('success2')
            print('phone ')
            print(form.cleaned_data['phone'])
            form.save(commit=True)
            return redirect('login')
    else :
        form = UserCreationForm()

    context['form'] = form

    return render(request, 'account/register.html', context)    