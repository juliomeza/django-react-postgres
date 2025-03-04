# Generated by Django 5.1.6 on 2025-02-18 15:27

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('logistics', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('lookup_code', models.CharField(max_length=50, unique=True)),
                ('notes', models.TextField(blank=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='enterprises', to='logistics.address')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_modified', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='enterprises', to='common.status')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='owners', to='enterprise.enterprise')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('lookup_code', models.CharField(max_length=50, unique=True)),
                ('orders_prefix', models.CharField(help_text='Unique prefix for order numbers', max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('notes', models.TextField(blank=True)),
                ('carriers', models.ManyToManyField(blank=True, related_name='projects', to='logistics.carrier')),
                ('contacts', models.ManyToManyField(blank=True, related_name='projects', to='logistics.contact')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='enterprise.enterprise')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_modified', to=settings.AUTH_USER_MODEL)),
                ('services', models.ManyToManyField(blank=True, related_name='projects', to='logistics.carrierservice')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='common.status')),
                ('warehouses', models.ManyToManyField(blank=True, related_name='projects', to='logistics.warehouse')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
