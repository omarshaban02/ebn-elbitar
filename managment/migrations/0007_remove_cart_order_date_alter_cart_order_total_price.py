# Generated by Django 4.2.2 on 2023-06-18 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0006_remove_user_image_alter_customers_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='order_date',
        ),
        migrations.AlterField(
            model_name='cart',
            name='order_total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
