# Generated by Django 3.2.8 on 2021-10-24 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_Desc',
            new_name='item_desc',
        ),
    ]
