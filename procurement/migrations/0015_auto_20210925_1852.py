# Generated by Django 3.1.2 on 2021-09-25 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0014_auto_20210925_1830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eggqualitycheck',
            old_name='batch_id',
            new_name='batch',
        ),
    ]
