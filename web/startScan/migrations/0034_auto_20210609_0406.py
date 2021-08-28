# Generated by Django 3.1.6 on 2021-06-09 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0033_auto_20210609_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipaddress',
            name='is_cdn',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='ports',
            field=models.ManyToManyField(related_name='port', to='startScan.Port'),
        ),
        migrations.DeleteModel(
            name='IP',
        ),
    ]