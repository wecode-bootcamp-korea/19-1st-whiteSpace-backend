# Generated by Django 3.2 on 2021-04-19 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210415_1500'),
        ('reviews', '0002_auto_20210418_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='bundle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.bundleoption'),
        ),
        migrations.AddField(
            model_name='review',
            name='color_size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.colorsizeoption'),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
