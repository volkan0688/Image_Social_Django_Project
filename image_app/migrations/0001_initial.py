# Generated by Django 4.2.2 on 2023-07-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
