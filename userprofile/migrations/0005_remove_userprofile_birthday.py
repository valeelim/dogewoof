# Generated by Django 4.1.2 on 2022-11-02 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_alter_userprofile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birthday',
        ),
    ]
