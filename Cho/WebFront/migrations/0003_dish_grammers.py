# Generated by Django 3.0.8 on 2020-08-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebFront', '0002_dish_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='grammers',
            field=models.IntegerField(default=0, verbose_name='Граммовки'),
        ),
    ]
