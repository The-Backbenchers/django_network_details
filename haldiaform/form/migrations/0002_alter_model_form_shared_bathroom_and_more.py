# Generated by Django 4.2.3 on 2023-07-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_form_shared',
            name='bathroom',
            field=models.CharField(choices=[('attached', 'attached'), ('common', 'common')], max_length=100),
        ),
        migrations.AlterField(
            model_name='model_form_single',
            name='bathroom',
            field=models.CharField(choices=[('attached', 'attached'), ('common', 'common')], max_length=100),
        ),
    ]
