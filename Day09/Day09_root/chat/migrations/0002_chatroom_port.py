# Generated by Django 3.2.6 on 2021-08-29 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='port',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
