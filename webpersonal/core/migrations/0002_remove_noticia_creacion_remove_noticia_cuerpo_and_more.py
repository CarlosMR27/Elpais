# Generated by Django 4.0.5 on 2023-01-08 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='creacion',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='cuerpo',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='update',
        ),
    ]