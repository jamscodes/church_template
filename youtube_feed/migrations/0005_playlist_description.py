# Generated by Django 5.0.3 on 2024-03-25 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_feed', '0004_playlist_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='description',
            field=models.CharField(default='Blank descriptions', max_length=255),
            preserve_default=False,
        ),
    ]