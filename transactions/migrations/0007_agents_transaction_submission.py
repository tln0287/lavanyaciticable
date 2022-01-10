# Generated by Django 3.0.6 on 2020-05-30 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_reports_agent_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agents_transaction_submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('agent_id', models.IntegerField(default=0, null=True)),
                ('agent_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bills_collected', models.CharField(blank=True, max_length=255, null=True)),
                ('amount_collected', models.CharField(blank=True, max_length=60, null=True)),
                ('amount_status', models.CharField(blank=True, max_length=60, null=True)),
                ('comments', models.CharField(blank=True, max_length=200, null=True)),
                ('Date', models.DateField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
