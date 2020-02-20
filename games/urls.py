from django.urls import path
from .views import GameDetailView   
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', GameDetailView.as_view(), name='detail')
]