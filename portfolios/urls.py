from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio_detail', views.portfolio_details, name='portfolio_detail'),

]