from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'portfolios/index.html')

def portfolio_details(request):
    return render(request, 'portfolios/portfolio_detail.html')