from django.db import models
from django.contrib.auth.models import User
from Gamely.games.models import Game, Platform

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favoriteGame = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    favoritePlatform = models.ForeignKey(Platform, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(default='default.jpg', upload_to='player_pics')

    def __str__(self):
        return f'{self.user.username} Player' 
    