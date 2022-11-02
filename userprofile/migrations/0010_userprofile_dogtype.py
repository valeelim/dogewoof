# Generated by Django 4.1.2 on 2022-11-02 11:52

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_remove_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dogtype',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('item_key1', 'Item title 1.1'), ('item_key2', 'Item title 1.2'), ('item_key3', 'Item title 1.3'), ('item_key4', 'Item title 1.4'), ('item_key5', 'Item title 1.5')], default='item_key4', max_length=20),
        ),
    ]
