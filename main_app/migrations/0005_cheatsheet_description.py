# Generated by Django 3.2.9 on 2022-01-20 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheatsheet',
            name='description',
            field=models.TextField(default='No description available yet', max_length=250),
        ),
    ]