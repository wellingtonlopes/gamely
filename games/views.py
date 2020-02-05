from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Game

# Create your views here.
def index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})

def detail(request, game_title):
    for gt in Game.objects.all():
        if game_title.lower() == gt.title.lower():
            game = gt
            return render(request, 'games/detail.html', {'game': game})
    raise Http404()
     