# Generated by Django 4.2.2 on 2023-06-21 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0022_remove_product_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image3',
        ),
    ]
