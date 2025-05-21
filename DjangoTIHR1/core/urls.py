from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login_view, name='login'),
    path('logout', views.Logout_view, name='logout'),
    path('dashboard', views.Dashboard_view, name='dashboard'),
]