from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from .form import *
from portfolios.urls import *
from portfolios.views import *
from portfolios.templates.portfolios import *
# Create your views here.
<<<<<<< HEAD

def registerPage(request):
    form = CreateAccount()
    if request.method == "POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            user = form.save()
            # group = Group.objects.get(name='accountholder')
            # print("THIS IS WHAT YOU ARE LOOKING FOR", group)
            # user.groups.add(group)
            return redirect('index')
    context = {'form':form}
    return render(request, 'accounts/register.html', context)
=======
def login(request):
    return render(request, 'accounts/login.html')
>>>>>>> 786ba7e73211f63b60ac5be698eca4e7d749660d
