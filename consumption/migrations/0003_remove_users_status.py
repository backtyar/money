# Generated by Django 4.2.7 on 2023-11-18 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumption', '0002_consumption_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='status',
        ),
    ]