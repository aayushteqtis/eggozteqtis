# Generated by Django 3.1.2 on 2021-09-25 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0013_auto_20210925_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eggsin',
            name='batch_id',
        ),
        migrations.AddField(
            model_name='eggsin',
            name='batch',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='procurement.batchmodel'),
        ),
    ]
