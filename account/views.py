from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')  # Redirect to the home page or any other page
            
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})
    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('index')
        
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')