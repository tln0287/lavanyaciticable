# Generated by Django 3.0.6 on 2020-06-01 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newuser', '0002_agent_stlicings_splicing'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Agent_stlicings',
            new_name='Agent_splicings',
        ),
        migrations.RenameField(
            model_name='agent_splicings',
            old_name='no_of_stlicings',
            new_name='no_of_splicings',
        ),
        migrations.AlterModelTable(
            name='agent_splicings',
            table='Agent_splicings',
        ),
    ]
