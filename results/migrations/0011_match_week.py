# Generated by Django 3.2.8 on 2023-04-27 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0010_remove_match_old_stats'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='week',
            field=models.IntegerField(default=1),
        ),
    ]
