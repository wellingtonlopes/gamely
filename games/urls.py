from django.urls import path
from .views import GameDeleteView, GameDetailView, GameListView, GameCreateView, GameUpdateView
from . import views

app_name = 'games'

urlpatterns = [
    path('', GameListView.as_view(), name='index'),
    path('games/<slug:slug>/delete', GameDeleteView.as_view(), name='delete'),
    path('games/new/', GameCreateView.as_view(), name='create'),
    path('games/<slug:slug>/update/', GameUpdateView.as_view(), name='update'),
    path('games/<slug:slug>/', GameDetailView.as_view(), name='detail'),
]