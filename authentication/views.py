from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect login after successful signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to your to home after successful login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
