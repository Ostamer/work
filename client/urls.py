from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='mainpage'),
    path('assessment/', views.assessment, name='assessment'),
    path('design/', views.design, name='design'),
    path('build/', views.build, name='build'),
    path('projects/', views.projects, name='projects'),
    path('ajax/submit-client/', views.ajax_submit_client, name='ajax_submit_client'),
]