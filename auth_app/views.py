from django.shortcuts import render, redirect
from .forms import SignUpForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username=name, password=user_password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You are logged in successfully')
                return redirect('profile')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def profile(request):
    user = request.user
    print(user)
    return render(request, 'profile.html', {'user': user})


def logout_user(request):
    logout(request)
    messages.success(request, 'You are loggedout successfully')
    return redirect('home')


def change_password_with_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'password.html', {'form': form})
    else:
        return redirect('login')


def change_password_without_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'password.html', {'form': form})
    else:
        return redirect('login')
