# Generated by Django 3.0.6 on 2020-08-10 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_transactiontotal'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TransactionTotal',
        ),
    ]
