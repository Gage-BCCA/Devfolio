from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, 'portfolios/forms/portfolio_form.html', {'form': form})

@login_required
def project_create(request):

    # If the portfolio can't be found, error out because we can't get any 
    # further in either case of a POST or a GET request
    target_portfolio = get_object_or_404(Portfolio, user=request.user)

    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project(
                portfolio=target_portfolio,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                blurb=form.cleaned_data.get('blurb'),
                programming_language=form.cleaned_data.get('programming_language'),
                project_link=form.cleaned_data.get('project_link')
            )
            project.save()
            return redirect('index')
    return render(request, 'portfolios/forms/project_form.html', {'form': form})

def skill_create(request):

    # If the portfolio can't be found, error out because we can't get any 
    # further in either case of a POST or a GET request
    target_portfolio = get_object_or_404(Portfolio, user=request.user)

    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            new_skill = Skill(
                portfolio=target_portfolio,
                skill_name=form.cleaned_data.get('skill_name'),
                experience_level=form.cleaned_data.get('experience_level')
            )
            new_skill.save()
            return redirect('index')
    return render(request, 'portfolios/forms/skill_form.html', {'form': form})

@login_required
def bio_create(request):

    # If the portfolio can't be found, error out because we can't get any 
    # further in either case of a POST or a GET request
    target_portfolio = get_object_or_404(Portfolio, user=request.user)

    form = BioForm()
    if request.method == 'POST':
        form = BioForm(request.POST)
        if form.is_valid():

            # Manually grab data
            name = form.cleaned_data.get('name')
            bio = form.cleaned_data.get('bio')
            location = form.cleaned_data.get('location')

            new_bio = Bio(
                portfolio=target_portfolio,
                name=name,
                location=location,
                bio=bio
            )
            new_bio.save()
            return redirect('index')
        
    context = {
        'form': form,
        'portfolio': target_portfolio
    }
    return render(request, 'portfolios/forms/bio_form.html', context=context)

def link_create(request):
    # If the portfolio can't be found, error out because we can't get any 
    # further in either case of a POST or a GET request
    target_portfolio = get_object_or_404(Portfolio, user=request.user)
    bio = target_portfolio.bio

    form = LinkForm()
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            new_link = Link(
                bio=bio,
                link_type=form.cleaned_data.get('link_type'),
                url=form.cleaned_data.get('url')
            )
            new_link.save()
            return redirect('index')
    return render(request, 'portfolios/forms/link_form.html', {'form': form})


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
        
    # Build context
    context['portfolio'] = portfolio
    context['projects'] = projects
    context['skills'] = skills
    context['links'] = links
    context['bio'] = bio

    # If any item is left empty, our portfolio is not yet completed
    portfolio_completed = True
    for item in context:
        if context[item] == None:
            portfolio_completed = False
            break
    
    # Use this variable to help conditionally render the landing page
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
    bio = portfolio.bio
    skills = portfolio.skill_set.all()
    projects = portfolio.project_set.all()
    links = bio.link_set.all()
    context = {
        'portfolio': portfolio,
        'bio': bio,
        'skills': skills,
        'projects': projects,
        'links': links
    }
    return render(request, 'portfolios/portfolio_detail.html', context=context)









































def example_delete_me(request):
    return render(request, "portfolios/example_portfolio.html")