# Generated by Django 4.2.2 on 2023-06-17 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0002_alter_cart_order_date_alter_customers_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='prduct_item',
            field=models.ManyToManyField(null=True, to='managment.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='prduct_item',
            field=models.ManyToManyField(null=True, to='managment.product'),
        ),
    ]
