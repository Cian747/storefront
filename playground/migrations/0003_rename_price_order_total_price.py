# Generated by Django 5.0.1 on 2024-03-07 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_rename_products_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='price',
            new_name='total_price',
        ),
    ]
