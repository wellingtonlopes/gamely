from django.shortcuts import render
from django.http import HttpResponse

def profile(request):
    return HttpResponse('<h1>Profile</h1>')
