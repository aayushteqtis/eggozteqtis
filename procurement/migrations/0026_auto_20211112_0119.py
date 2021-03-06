# Generated by Django 3.1.2 on 2021-11-11 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0025_batchmodel_actual_egg_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='eggqualitycheck',
            name='avg_weight',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='eggqualitycheck',
            name='chatki_percent',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='eggqualitycheck',
            name='dirty_percent',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='eggqualitycheck',
            name='egg_color_unit',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='eggqualitycheck',
            name='egg_ph',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='eggqualitycheck',
            name='egg_used',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='eggqualitycheck',
            name='haught_unit',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='eggqualitycheck',
            name='shape_size_percent',
            field=models.FloatField(default=0),
        ),
    ]
