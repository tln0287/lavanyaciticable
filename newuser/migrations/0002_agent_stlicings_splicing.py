# Generated by Django 3.0.6 on 2020-06-01 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent_stlicings',
            name='splicing',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]