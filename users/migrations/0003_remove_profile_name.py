# Generated by Django 3.2.2 on 2021-05-16 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
