# Generated by Django 3.0.2 on 2020-02-03 13:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='release_year',
        ),
        migrations.AddField(
            model_name='game',
            name='release_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]