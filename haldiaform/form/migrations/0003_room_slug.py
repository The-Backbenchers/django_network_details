# Generated by Django 4.2.3 on 2023-07-18 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_alter_room_options_remove_room_created_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(default=None, max_length=200, unique=True),
        ),
    ]