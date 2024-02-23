from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    # put html tags in this or it displays it as standard text
    return HttpResponse("<h1>Hello World</h1>")

def v1(response):
    # put html tags in this 
    return HttpResponse("<h1>View 1</h1>")