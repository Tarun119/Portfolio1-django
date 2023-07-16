from main import views
from django.urls import path

urlpatterns = [
    path('languages/',views.languages,name='languages'),
    path('projects/',views.projects,name='projects'),
    path('index/',views.index,name='index'),
]