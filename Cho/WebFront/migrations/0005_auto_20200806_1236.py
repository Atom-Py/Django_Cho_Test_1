# Generated by Django 3.0.8 on 2020-08-06 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebFront', '0004_auto_20200806_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Стоимость заказа'),
        ),
    ]
