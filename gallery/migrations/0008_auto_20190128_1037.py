# Generated by Django 2.1.3 on 2019-01-28 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_gallery_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='image_360Link',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='is_360',
        ),
    ]
