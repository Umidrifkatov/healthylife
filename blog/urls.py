from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('mission/', views.mission, name='mission'),
    # path('projects/', views.projects, name='projects'),
]