# Generated by Django 5.1.3 on 2024-12-02 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='api_key',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='secret_key',
        ),
    ]