# login/urls.py
from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('employer/', views.employer_view, name='employer'),
    path('job-seeker/', views.job_seeker_view, name='job_seeker'),
]