# Generated by Django 3.0.6 on 2020-06-01 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cable', '0008_auto_20200526_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='flag',
            field=models.IntegerField(default=0, null=True),
        ),
    ]