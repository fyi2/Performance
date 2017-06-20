# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
        UserCreationForm,
        UserChangeForm,
        PasswordChangeForm
        )
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render, redirect
from acct.forms import ( EditAccountForm, SignUpForm,
                        ProfileForm
                        )
from acct.models import UserProfile
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# Create your views here.

def view_profile(request):
    form = UserProfile.objects.get(user=request.user)
    args = {'form':form}
    return render(request,'acct/profile.html',args)


def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            save_data = form.save(commit=False)
            save_data.user = request.user
            save_data.save()
            return redirect(reverse('acct:profile'))
    else:
        udata = UserProfile.objects.get(user=request.user)
        form = ProfileForm(instance=udata)
        args = {'form': form}
    return render(request, 'acct/edit_profile.html', args)

@login_required
def index(request):
    return render(request,"acct/home.html", {})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request,"acct/home.html", {})
    else:
        form = SignUpForm()
    return render(request, 'acct/signup.html', {'form': form})

def edit_account(request):
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request,"acct/account.html", {})
    else:
        form = EditAccountForm(instance=request.user)
        args = {'form':form}
        return render(request,'acct/edit_account.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request,"acct/profile.html", {})
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request,'acct/change_password.html', args)
    return render(request, 'acct/change_password.html', {'form1': form})

def account(request):
    args = {'user':request.user}
    return render(request, 'acct/account.html', args)
