from django.shortcuts import render, redirect
from .forms import PortfolioForm, ProjectForm, SkillForm, BioForm, LinkForm
# Create your views here.
def index(request):
    return render(request, 'portfolios/index.html')

def portfolio_create(request):
    form = PortfolioForm()
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'portfolios/portfolio_form.html', {'form': form})

def project_create(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'portfolios/project_form.html', {'form': form})

def skill_create(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'portfolios/skill_form.html', {'form': form})

def bio_create(request):
    form = BioForm()
    if request.method == 'POST':
        form = BioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'portfolios/bio_form.html', {'form': form})

def link_create(request):
    form = LinkForm()
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'portfolios/link_form.html', {'form': form})







































def example_delete_me(request):
    return render(request, "portfolios/example_portfolio.html")
def portfolio_details(request):
    return render(request, 'portfolios/portfolio_detail.html')









































def example_delete_me(request):
    return render(request, "portfolios/example_portfolio.html")