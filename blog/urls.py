from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='blog-home'),
    path('post/<str:slug>/', views.post_detail, name='post_detail_url'),
    path('about/', views.about, name='about'),
    # path('mission/', views.mission, name='mission'),
    # path('projects/', views.projects, name='projects'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)