# Generated by Django 3.2.9 on 2021-11-23 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20211123_0007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experts',
            old_name='satcks',
            new_name='stacks',
        ),
    ]
