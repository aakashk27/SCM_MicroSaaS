# Generated by Django 5.1.1 on 2024-09-11 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('demand_forecast', models.PositiveIntegerField(help_text='Demand forecast per unit of time')),
            ],
        ),
        migrations.CreateModel(
            name='DistributionCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('max_storage_capacity', models.PositiveIntegerField()),
                ('current_stock', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('max_capacity', models.PositiveIntegerField()),
                ('production_rate', models.DecimalField(decimal_places=2, help_text='Production rate per unit of time', max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=50)),
                ('max_load_capacity', models.PositiveIntegerField()),
                ('cost_per_km', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('volume', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Price per unit in Rupees', max_digits=10)),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Backend.factory')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(blank=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='Backend.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='Backend.product')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.PositiveIntegerField(default=0)),
                ('distribution_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventories', to='Backend.distributioncenter')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventories', to='Backend.product')),
            ],
        ),
    ]
