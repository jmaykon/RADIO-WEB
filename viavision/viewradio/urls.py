from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('programas/', views.programas, name='programas'),
    path('inmobiliaria/', views.inmobiliaria, name='inmobiliaria'),
    path('studio-live/', views.studio_live, name='studio_live'),
    path('contacto/', views.contacto, name='contacto'),
]