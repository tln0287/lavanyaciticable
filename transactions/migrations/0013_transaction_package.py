# Generated by Django 3.0.6 on 2021-03-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0012_auto_20210314_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='package',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
