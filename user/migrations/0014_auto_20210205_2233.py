# Generated by Django 3.1.5 on 2021-02-05 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20210205_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turf',
            name='sport',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='turf',
            name='timePeriod',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='turf',
            name='turfName',
            field=models.TextField(blank=True, null=True),
        ),
    ]
