from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView, ListView, DetailView, CreateView, UpdateView
from .models import Game

# Create your views here.
""" def index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games}) """

""" def detail(request, game_title):
    for gt in Game.objects.all():
        if game_title.lower() == gt.title.lower():
            game = gt
            return render(request, 'games/detail.html', {'game': game, 'title':game.title})
    raise Http404() """

class GameDetailView(DetailView):
    model = Game
    template_name = 'games/detail.html'
    slug_url_kwarg = 'slug'

class GameListView(ListView):
    model = Game
    template_name = 'games/index.html'
    context_object_name = 'games'
    ordering = ['title']

class GameCreateView(LoginRequiredMixin, CreateView):
    model = Game
    fields = ['title', 'genre', 'developer', 'publisher', 'platform', 'release_date', 'image']

class GameUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Game
    fields = ['title', 'genre', 'developer', 'publisher', 'platform', 'release_date', 'image']

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

class GameDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Game
    success_url = '/'

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False