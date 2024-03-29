# Generated by Django 5.0.3 on 2024-03-14 19:41

import youtube_feed.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_feed', '0002_alter_playlist_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='link',
            field=models.CharField(max_length=255, validators=[youtube_feed.validators.validate_playlist_link_contains_list_id]),
        ),
    ]
