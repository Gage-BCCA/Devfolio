from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-portfolio/', views.create_portfolio, name='create_portfolio'),
    path('portfolio/', views.portfolio_detail, name='portfolio_detail'),
]