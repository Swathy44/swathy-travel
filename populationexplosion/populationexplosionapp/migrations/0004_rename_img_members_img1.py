# Generated by Django 4.1.5 on 2023-01-25 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populationexplosionapp', '0003_members_delete_team_members'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='img',
            new_name='img1',
        ),
    ]
