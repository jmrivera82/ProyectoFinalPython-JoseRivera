# Generated by Django 3.2.24 on 2024-03-19 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto', '0005_consolas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consolas',
            old_name='Empresa',
            new_name='empresa',
        ),
    ]
