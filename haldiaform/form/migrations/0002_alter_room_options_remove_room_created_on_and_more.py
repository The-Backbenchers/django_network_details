# Generated by Django 4.2.3 on 2023-07-18 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={},
        ),
        migrations.RemoveField(
            model_name='room',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='room',
            name='slug',
        ),
    ]
