from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio_detail', views.portfolio_details, name='portfolio_detail'),
    path('portfolio/create/', views.portfolio_create, name='portfolio_create'),
    path('project/create/', views.project_create, name='project_create'),
    path('skill/create/', views.skill_create, name='skill_create'),
    path('bio/create/', views.bio_create, name='bio_create'),
    path('link/create/', views.link_create, name='link_create'),

    # Landing Pages
    path('landing/', views.employee_landing_view, name="employee_landing"),
    path('hiring/', views.employer_landing_view, name="employer_landing")

]