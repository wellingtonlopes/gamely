# Generated by Django 3.0.2 on 2020-02-03 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20200203_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
