# Generated by Django 3.0.3 on 2020-02-20 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_game_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='game_img'),
        ),
    ]
