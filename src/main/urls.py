from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('service/<slug>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('project/<slug>/', views.ProjectDetailView.as_view(), name='project_detail')
]
