# Generated by Django 4.1.2 on 2022-11-02 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_userprofile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]