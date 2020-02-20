# Generated by Django 3.0.3 on 2020-02-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_remove_game_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.SlugField(default='Wargroove', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
