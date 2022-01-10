# Generated by Django 3.0.6 on 2020-05-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('agent_id', models.IntegerField(default=0, null=True)),
                ('bills_collected', models.CharField(blank=True, max_length=255, null=True)),
                ('amount_collected', models.CharField(blank=True, max_length=60, null=True)),
                ('amount_status', models.CharField(blank=True, max_length=60, null=True)),
                ('comments', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('agent_id', models.IntegerField(default=0, null=True)),
                ('CAF_Number', models.CharField(blank=True, max_length=255, null=True)),
                ('txn_id', models.CharField(blank=True, max_length=15, null=True)),
                ('customer_mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('transaction_type', models.CharField(blank=True, max_length=60, null=True)),
                ('paid_amount', models.CharField(blank=True, max_length=60, null=True)),
                ('Date', models.CharField(blank=True, max_length=255, null=True)),
                ('createdon', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(default=1, null=True)),
            ],
        ),
    ]