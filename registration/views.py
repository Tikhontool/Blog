from .forms import RegisterForm, MyPasswordChangeForm, UserForgotPasswordForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect



def home_page(requests):
    return render(requests, 'registration/base.html')

def sign_up(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = MyPasswordChangeForm(request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, ('Your password was successfully updated!'))
            return redirect('accounts:change_password')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        form = MyPasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})