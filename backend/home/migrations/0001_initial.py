# Generated by Django 3.2.9 on 2021-11-19 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('items', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Pack',
                'verbose_name_plural': 'Pack',
            },
        ),
        migrations.CreateModel(
            name='Premium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('Packitems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.pack')),
            ],
            options={
                'verbose_name': 'Premium',
                'verbose_name_plural': 'Premium',
            },
        ),
    ]
