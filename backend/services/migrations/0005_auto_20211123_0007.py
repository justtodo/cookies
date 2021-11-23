# Generated by Django 3.2.9 on 2021-11-23 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_experts_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='stacks',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='experts',
            name='note',
            field=models.IntegerField(default=3),
        ),
    ]
