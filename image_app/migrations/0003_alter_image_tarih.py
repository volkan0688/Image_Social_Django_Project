# Generated by Django 4.2.2 on 2023-07-11 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0002_image_tarih'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='tarih',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
