from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('register/', views.registerPage, name="register")
=======
    path('login/', views.login, name='login'),
>>>>>>> 786ba7e73211f63b60ac5be698eca4e7d749660d
]