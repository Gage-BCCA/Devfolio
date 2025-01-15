from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import PortfolioForm, ProjectForm, SkillForm, BioForm, LinkForm
from .models import Portfolio, Bio, Link, Skill, Project

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.user.account_set.all()[0].account_type == "employee":
            return redirect('employee_landing')
        
        return redirect('employer_landing')
    return render(request, 'portfolios/index.html')

def portfolio_create(request):
    form = PortfolioForm()
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            layout = form.cleaned_data.get('layout')
            color_theme = form.cleaned_data.get('color_theme')
            user = User.objects.get(pk=request.POST.get('user'))
            portfolio = Portfolio(
                user=user,
                layout=layout,
                color_theme=color_theme
            )
            portfolio.save()
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


@login_required
def employee_landing_view(request):
    # Basic validation that non-employees can see this page
    if request.user.account_set.all()[0].account_type != "employee":
        return redirect('index')
    
    context = {}

    # Hacky ass ways to get an object or return none
    try:
        portfolio = Portfolio.objects.get(user=request.user)
    except Portfolio.DoesNotExist:
        portfolio = None

    if portfolio is not None:
        try:
            bio = Bio.objects.get(portfolio=portfolio)
        except Bio.DoesNotExist:
            bio = None
        
        try:
            projects = Project.objects.get(portfolio=portfolio)
        except Project.DoesNotExist:
            projects = None
        
        try:
            skills = Skill.objects.get(portfolio=portfolio)
        except Skill.DoesNotExist:
            skills = None
        
        try:
            links = Link.objects.get(bio=bio)
        except Link.DoesNotExist:
            links = None
        
    context['portfolio'] = portfolio
    context['projects'] = projects
    context['skills'] = skills
    context['links'] = links
    context['bio'] = bio

    portfolio_completed = True
    for item in context:
        if context[item] == None:
            portfolio_completed = False

    context["is_portfolio_complete"] = portfolio_completed 
    return render(request, "portfolios/landings/employee_landing.html", context=context)

@login_required
def employer_landing_view(request):
    print(request.user.account_set.all()[0].account_type)

    # Basic validation that non-employers can see this page
    if request.user.account_set.all()[0].account_type != "employer":
        return redirect('index')
    
    return render(request, "portfolios/landings/employer_landing.html")

def portfolio_view(request, username):
    user = User.objects.get(username=username)
    portfolio = Portfolio.objects.get(user=user)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'portfolios/portfolio_detail.html')

































def example_delete_me(request):
    return render(request, "portfolios/example_portfolio.html")
def portfolio_details(request):
    return render(request, 'portfolios/portfolio_detail.html')









































def example_delete_me(request):
    return render(request, "portfolios/example_portfolio.html")