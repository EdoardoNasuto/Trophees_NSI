# Generated by Django 3.2.8 on 2023-05-14 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0010_team_matches_played'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='MMR',
        ),
        migrations.RemoveField(
            model_name='player',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='team',
            name='logo',
        ),
    ]
