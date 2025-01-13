from django.shortcuts import render, redirect
from .models import Portfolio
from .forms import PortfolioForm
from accounts.views import *

# Create your views here.
def index(request):
    return render(request, 'portfolios/index.html')

def portfolio_detail(request):
    portfolio = Portfolio.objects.get(account = request.user.account)
    return render(request, 'portfolios/portfolio_detail.html', {'portfolio': portfolio})

def create_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False) # don't save it to the database yet
            portfolio.account = request.user.account
            portfolio.save()
            return redirect('portfolio_detail')
    else:
        form = PortfolioForm()
    return render(request, 'portfolios/create_portfolio.html', {'form': form})