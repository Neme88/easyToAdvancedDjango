from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World. This is the index view of my first app.")


# Create your views here.
