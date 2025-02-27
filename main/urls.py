from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.notes, name='notes'),
    path('pastpaper/', views.pastpaper, name='pastpaper'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('examtips/', views.examtips, name='examtips')
]
