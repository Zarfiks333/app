from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from user.forms import *

def login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    
    else:
        form = UserLoginForm()

    context = {
        'title': 'BuldMMO | Вход',
        'form': form,
    }

    return render(request, 'user/login.html', context)

def registration(request):

    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'BuldMMO | Регистрация',
        'form': form,
    }

    return render(request, 'user/registration.html', context)

@login_required
def profile(request):

    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    
    else:
        form = ProfileForm( instance=request.user )

    context = {
        'form': form,
    }

    return render(request, 'user/profile.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))
