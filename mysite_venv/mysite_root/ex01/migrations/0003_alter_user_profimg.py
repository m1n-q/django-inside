# Generated by Django 3.2.6 on 2021-09-02 03:36

from django.db import migrations, models
import ex01.models


class Migration(migrations.Migration):

    dependencies = [
        ('ex01', '0002_auto_20210902_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profimg',
            field=models.ImageField(null=True, upload_to=ex01.models.User.path_file_name),
        ),
    ]
