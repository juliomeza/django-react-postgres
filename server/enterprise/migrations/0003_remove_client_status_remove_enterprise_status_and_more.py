# Generated by Django 5.1.6 on 2025-02-18 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0002_remove_project_enterprise_client_project_client_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='status',
        ),
        migrations.RemoveField(
            model_name='enterprise',
            name='status',
        ),
        migrations.RemoveField(
            model_name='project',
            name='status',
        ),
        migrations.AddField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='enterprise',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
