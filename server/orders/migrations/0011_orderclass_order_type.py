# Generated by Django 5.1.6 on 2025-02-19 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_orderstatus_created_by_orderstatus_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderclass',
            name='order_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='order_classes', to='orders.ordertype'),
            preserve_default=False,
        ),
    ]
