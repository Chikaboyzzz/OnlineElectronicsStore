# Generated by Django 4.2 on 2023-05-16 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_customer_employee_order_remove_product_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='amount',
        ),
    ]
