# Generated by Django 3.2 on 2021-04-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mileage',
            field=models.PositiveIntegerField(default=0),
        ),
    ]