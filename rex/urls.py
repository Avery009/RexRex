from . import views
from django.urls import path, include

urlpatterns = [
	path('', views.home, name = 'Rex'),
	path('projects/', views.projects, name = 'Projects'),
    path('deboos/', views.deboos, name = 'Deboos'),
	path('contractr/', views.contractr, name = 'Contractr'),
    path('curatr/', views.curatr, name = 'Curatr'),
    path('votr/', views.votr, name = 'Votr'),
    path('docify/', views.docify, name = 'Docify'),
    path('acronymify/', views.acronymify, name = 'Acronymify'),
] 