from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("customer_profile/<int:pk>/", views.customer_profile, name="customer_profile"),
    path("add_record", views.add_record, name="add_record"),
]