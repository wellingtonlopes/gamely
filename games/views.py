from django.http import HttpResponse
from django.shortcuts import render
from .models import Game

# Create your views here.
def index(request):
    games = Game.objects.all()
    return render(request, 'index.html', { 'games': games })