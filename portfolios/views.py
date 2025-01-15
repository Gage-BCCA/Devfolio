from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'portfolios/index.html')









































def example_delete_me(request):
    return render(request, "portfolios/example_portfolio.html")