# Generated by Django 3.0.6 on 2020-11-19 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0009_delete_transactiontotal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agents_transaction_submission',
            options={'verbose_name_plural': 'Agents transaction submission'},
        ),
        migrations.AlterModelOptions(
            name='reports',
            options={'verbose_name_plural': 'Reports'},
        ),
    ]