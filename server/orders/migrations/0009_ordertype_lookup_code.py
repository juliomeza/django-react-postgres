# Generated by Django 5.1.6 on 2025-02-19 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_orderstatus_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertype',
            name='lookup_code',
            field=models.CharField(default=1, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
