# Generated by Django 3.2.2 on 2021-05-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210508_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='placeholder.jpg', upload_to='images'),
        ),
    ]
