from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.post_list, name='blog-home'),
    path('post/<str:slug>/', views.post_detail, name='post_detail_url'),
    path('about/', views.about, name='about'),
    # path('mission/', views.mission, name='mission'),
    # path('projects/', views.projects, name='projects'),
]
