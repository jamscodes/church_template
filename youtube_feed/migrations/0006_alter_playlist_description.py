# Generated by Django 5.0.3 on 2024-03-25 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_feed', '0005_playlist_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='description',
            field=models.TextField(),
        ),
    ]
