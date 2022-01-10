# Generated by Django 3.0.6 on 2020-06-21 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_agents_transaction_submission'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('agent_id', models.IntegerField(default=0, null=True)),
                ('agent_name', models.CharField(blank=True, max_length=255, null=True)),
                ('CAF_Number', models.CharField(blank=True, max_length=255, null=True)),
                ('txn_id', models.CharField(blank=True, max_length=15, null=True)),
                ('customer_mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=60, null=True)),
                ('transaction_type', models.CharField(blank=True, max_length=60, null=True)),
                ('paid_amount', models.CharField(blank=True, max_length=60, null=True)),
                ('balance_amount', models.CharField(blank=True, max_length=60, null=True)),
                ('Date', models.DateField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
