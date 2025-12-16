
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name=""),
    path('login',views.login, name="login"),
    path('register',views.register, name="register"),
    path('user_logout', views.user_logout, name="user_logout"),
    path('carbon_foorprint', views.carbon_footprint, name="carbon_footprint"),
    path('energy', views.energy, name="energy"),
]
