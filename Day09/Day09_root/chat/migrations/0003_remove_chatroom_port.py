# Generated by Django 3.2.6 on 2021-09-01 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chatroom_port'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='port',
        ),
    ]
