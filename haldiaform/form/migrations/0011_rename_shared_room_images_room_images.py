# Generated by Django 4.2.3 on 2023-07-19 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0010_shared_room_images'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='shared_room_images',
            new_name='room_images',
        ),
    ]