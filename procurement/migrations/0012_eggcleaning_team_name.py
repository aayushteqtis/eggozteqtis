# Generated by Django 3.1.2 on 2021-09-24 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0011_auto_20210925_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='eggcleaning',
            name='team_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
