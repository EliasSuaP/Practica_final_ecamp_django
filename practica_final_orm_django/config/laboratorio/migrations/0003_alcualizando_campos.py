# Generated by Django 4.0.5 on 2023-07-23 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0002_rename_laboratorio_directorgeneral_laboratorio'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorgeneral',
            name='especialidad',
            field=models.CharField(default='nulo', max_length=100),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='ciudad',
            field=models.CharField(default='nulo', max_length=100),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='pais',
            field=models.CharField(default='nulo', max_length=100),
        ),
    ]
