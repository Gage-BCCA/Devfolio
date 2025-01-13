from django.shortcuts import render
from accounts.views import *

# Create your views here.
def index(request):
    return render(request, 'portfolios/index.html')