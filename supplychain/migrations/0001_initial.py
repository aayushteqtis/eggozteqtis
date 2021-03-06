# Generated by Django 3.1.2 on 2021-09-11 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplyPersonProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('management_status', models.CharField(choices=[('Manager', 'Manager'), ('Regional Manager', 'Regional Manager'), ('Worker', 'Worker')], default='Worker', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='supply', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
