#we are defining the paths to different web pages

from django.urls import path 
from . import views

urlpatterns = [
    path("<str:name>",views.index,name="index"), 
]