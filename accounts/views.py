from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import *
from .form import *
from portfolios.urls import *
from portfolios.views import *
from portfolios.templates.portfolios import *
# Create your views here.

def register_page(request):
    form = CreateAccount()
    if request.method == "POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            account_type = form.cleaned_data.get('account_type')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('password2')
            if password == password2:
                new_account = Account(name=name, account_type=account_type, email=email, phone=phone, password=password, password2=password2)
                new_account.save()
            else:
                messages.info(request, "Passwords do not match")
        return redirect('index')
    context = {'form':form}
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('portfolio_detail')
    return render(request, 'accounts/login.html')
