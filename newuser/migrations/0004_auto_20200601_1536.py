# Generated by Django 3.0.6 on 2020-06-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newuser', '0003_auto_20200601_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent_splicings',
            name='splicing',
            field=models.CharField(blank=True, default='0', max_length=255),
        ),
    ]
