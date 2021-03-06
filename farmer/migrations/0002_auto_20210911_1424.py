# Generated by Django 3.1.2 on 2021-09-11 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('supplychain', '0001_initial'),
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='supplyPerson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supply_manager', to='supplychain.supplypersonprofile'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='farmer_expenses', to='farmer.farmer'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='farmer_expenses', to='farmer.party'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='productSubDivision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='farmer_expenses', to='product.productsubdivision'),
        ),
        migrations.AddField(
            model_name='dailyinput',
            name='flock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='dailyinputs', to='farmer.flock'),
        ),
        migrations.AddField(
            model_name='dailyinput',
            name='transferred_input',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='transferredInput', to='farmer.transferredbirdinput'),
        ),
        migrations.AddField(
            model_name='cityneccrate',
            name='necc_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='necc_city_rate', to='farmer.necccity'),
        ),
        migrations.AlterUniqueTogether(
            name='postlike',
            unique_together={('user', 'post')},
        ),
        migrations.AlterUniqueTogether(
            name='postcommentlike',
            unique_together={('user', 'post_comment')},
        ),
        migrations.AlterUniqueTogether(
            name='farmerorderinline',
            unique_together={('farmerOrder', 'egg_type')},
        ),
        migrations.AlterUniqueTogether(
            name='dailyinput',
            unique_together={('flock', 'date')},
        ),
    ]
