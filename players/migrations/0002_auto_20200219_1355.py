# Generated by Django 3.0.3 on 2020-02-19 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(default='default.png', upload_to='player_pics'),
        ),
    ]