from django.contrib import admin
from .models import Genre, Game, Publisher, Developer, Platform

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Genre, GenreAdmin)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Publisher, PublisherAdmin)

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Developer, DeveloperAdmin)

class PlatformAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Platform, PlatformAdmin)

class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genres', 'platforms','developer')
    prepopulated_fields = {'slug': ('title', )}
admin.site.register(Game, GameAdmin)