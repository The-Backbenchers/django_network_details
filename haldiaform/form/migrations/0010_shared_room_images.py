# Generated by Django 4.2.3 on 2023-07-19 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0009_remove_room_no_of_rooms_remove_room_phone_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='shared_room_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.room')),
            ],
        ),
    ]
