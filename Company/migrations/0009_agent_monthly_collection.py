# Generated by Django 3.0.6 on 2021-01-27 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0008_auto_20201119_0703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent_monthly_collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('agent_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.CharField(blank=True, max_length=255, null=True)),
                ('total_cash_collected', models.CharField(blank=True, max_length=255, null=True)),
                ('total_phonepe_collected', models.CharField(blank=True, max_length=255, null=True)),
                ('total_gpay_collected', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Agent_monthly_collection',
            },
        ),
    ]
