# Generated by Django 5.1.3 on 2024-11-07 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='image',
            table='image',
        ),
        migrations.AlterModelTable(
            name='videoreview',
            table='videoreviews',
        ),
    ]
