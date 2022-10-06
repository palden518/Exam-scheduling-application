from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('dashboard.html', views.dashboard, name='dashboard'),
    path('examination.html', views.examination, name='examination'),
    path('EditTimetable.html', views.EditTimetable, name='EditTimetable'),
    path('profile.html', views.profile, name='profile')
]

