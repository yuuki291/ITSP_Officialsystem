# Generated by Django 3.1.2 on 2021-02-24 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mstusers',
            old_name='CompanyId',
            new_name='Company',
        ),
    ]
