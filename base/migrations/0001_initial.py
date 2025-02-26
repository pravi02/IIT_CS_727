# Generated by Django 5.0.7 on 2025-02-05 17:27

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('serial_no', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=50)),
                ('product_weight', models.FloatField()),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_location', models.CharField(max_length=100)),
                ('customer_email', models.CharField(max_length=100)),
                ('customer_telephone', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'customer',
                'unique_together': {('customer_name', 'customer_location', 'customer_telephone')},
            },
        ),
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(default=datetime.datetime.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.customer')),
            ],
            options={
                'db_table': 'customer_order',
            },
        ),
        migrations.CreateModel(
            name='CustomerOrderItems',
            fields=[
                ('line_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('request_quantity', models.IntegerField()),
                ('customer_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.customerorder')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
            ],
            options={
                'db_table': 'customer_order_items',
            },
        ),
        migrations.CreateModel(
            name='InventoryLocation',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('aisle_number', models.CharField(max_length=50)),
                ('bin_location', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'inventory_location',
                'unique_together': {('aisle_number', 'bin_location')},
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventory_id', models.AutoField(primary_key=True, serialize=False)),
                ('available_quantity', models.IntegerField()),
                ('inventory_status', models.BooleanField(default=True)),
                ('inventory_location', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.inventorylocation')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.product')),
            ],
            options={
                'db_table': 'inventory',
                'unique_together': {('product', 'inventory_location')},
            },
        ),
        migrations.CreateModel(
            name='OrderProcess',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_date', models.DateField()),
                ('sales_amount', models.FloatField()),
                ('order_processed', models.BooleanField(default=False)),
                ('customer_order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.customer')),
                ('processed_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'order_process',
            },
        ),
        migrations.CreateModel(
            name='ProcessedLineItems',
            fields=[
                ('line_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('allocated_quantity', models.IntegerField()),
                ('customer_line_item', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.customerorderitems')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.inventory')),
                ('process_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.orderprocess')),
            ],
            options={
                'db_table': 'processed_line_items',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'product_category',
                'unique_together': {('category_name',)},
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.productcategory'),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=50)),
                ('supplier_contact_number', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'supplier',
                'unique_together': {('supplier_name', 'supplier_contact_number')},
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.supplier'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('product_name', 'product_category')},
        ),
    ]
