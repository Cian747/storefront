# Generated by Django 5.0.1 on 2024-03-07 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0003_rename_price_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default=0, max_length=50),
        ),
    ]
