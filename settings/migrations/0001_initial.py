# Generated by Django 5.1.3 on 2024-11-07 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('contact_whatsapp', models.CharField(blank=True, max_length=20, null=True)),
                ('contact_telegram', models.CharField(blank=True, max_length=50, null=True)),
                ('work_schedule', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
