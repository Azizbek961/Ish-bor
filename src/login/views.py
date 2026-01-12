# login/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Xush kelibsiz, {username}!')
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                messages.error(request, 'Login yoki parol noto\'g\'ri')
        else:
            messages.error(request, 'Login yoki parol noto\'g\'ri')
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Siz tizimdan chiqdingiz')
    return redirect('login')


@login_required
def profile_view(request):
    return render(request, 'login/profile.html')