# Generated by Django 3.1.2 on 2021-03-03 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20210303_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mstusers',
            name='id',
        ),
        migrations.AlterField(
            model_name='mstcompanys',
            name='CompanyId',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mstusers',
            name='UserId',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
