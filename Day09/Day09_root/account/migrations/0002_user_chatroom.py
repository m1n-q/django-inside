# Generated by Django 3.2.6 on 2021-08-29 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chatroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat.chatroom'),
        ),
    ]
