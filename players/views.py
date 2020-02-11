from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def profile(request):
    return HttpResponse('<h1>Profile</h1>')
