from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib import messages
from .models import *
from .form import *
from portfolios.urls import *
from portfolios.views import *
from portfolios.templates.portfolios import *
# Create your views here.

def register_page(request):
    # Pass in built-in Django Form
    form = RegisterForm()

    if request.method == "POST":

        # Grab the account type manually since it's
        # not part of the build in Django form
        account_type = request.POST.get('account-type')

        form = RegisterForm(request.POST)

        if form.is_valid():

            # Create user
            new_user = form.save(commit=False)
            new_user.username = new_user.username.lower()
            new_user.save()

            # Create related account
            new_account = Account(
                user = new_user,
                account_type = account_type
            )
            new_account.save()

            # Log the user in and redirect
            login(request, new_user)
            return redirect('index')
        
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username').lower(), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')