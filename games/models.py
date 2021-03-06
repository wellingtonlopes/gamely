from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from PIL import Image

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(default=timezone.now)
    slug = models.SlugField(max_length=100, unique=True)
    genre = models.ManyToManyField(Genre)
    platform = models.ManyToManyField(Platform)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    developer = models.ForeignKey(Developer,on_delete=models.PROTECT)
    image = models.ImageField(default='default.jpg', upload_to='game_img')

    def __str__(self):
        return self.title

    # methods below are used to display all 'ManyToMany' values of each field
    def genres(self):
        return ", ".join([g.name for g in self.genre.all()])

    def platforms(self):
        return ", ".join([p.name for p in self.platform.all()])

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)
        """ img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path) """
    
    def get_absolute_url(self):
        return reverse('games:detail', kwargs={'slug': self.slug})
    