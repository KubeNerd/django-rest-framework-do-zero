# Generated by Django 3.1 on 2020-08-28 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='create_at',
        ),
    ]