# Generated by Django 5.2 on 2025-04-23 22:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True)),
                ('active', models.BooleanField(db_column='is_active', default=True)),
                ('name', models.CharField(db_column='name', max_length=70)),
            ],
            options={
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True)),
                ('active', models.BooleanField(db_column='is_active', default=True)),
                ('name', models.CharField(db_column='name', max_length=70)),
                ('age', models.IntegerField(db_column='age')),
                ('cpf', models.CharField(db_column='cpf', max_length=12)),
            ],
            options={
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True)),
                ('active', models.BooleanField(db_column='is_active', default=True)),
                ('name', models.CharField(db_column='name', max_length=70)),
                ('registration', models.CharField(db_column='registration', max_length=15)),
            ],
            options={
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True)),
                ('active', models.BooleanField(db_column='is_active', default=True)),
                ('description', models.CharField(db_column='tx_description', max_length=100)),
                ('quantity', models.IntegerField(db_column='quantity')),
            ],
            options={
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True)),
                ('active', models.BooleanField(db_column='is_active', default=True)),
                ('title', models.CharField(db_column='title', max_length=200)),
                ('author', models.ForeignKey(db_column='author_id', on_delete=django.db.models.deletion.CASCADE, to='teste.author')),
            ],
            options={
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True)),
                ('active', models.BooleanField(db_column='is_active', default=True)),
                ('nrf', models.CharField(db_column='nrf', max_length=200)),
                ('client', models.ForeignKey(db_column='client_id', on_delete=django.db.models.deletion.CASCADE, to='teste.client')),
                ('employee', models.ForeignKey(db_column='employee_id', on_delete=django.db.models.deletion.CASCADE, to='teste.employee')),
                ('product', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='teste.product')),
            ],
            options={
                'abstract': False,
                'managed': True,
            },
        ),
    ]
