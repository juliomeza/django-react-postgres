# Generated by Django 5.1.6 on 2025-02-18 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0002_remove_project_enterprise_client_project_client_and_more'),
        ('users', '0002_role_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='users', to='enterprise.project'),
            preserve_default=False,
        ),
    ]
