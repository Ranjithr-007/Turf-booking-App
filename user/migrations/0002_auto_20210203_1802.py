# Generated by Django 3.1.5 on 2021-02-03 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='name',
        ),
        migrations.AddField(
            model_name='booking',
            name='paymentOption',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='badminton',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='cricket',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='football',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='facilities',
            name='bath',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='facilities',
            name='cafteria',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='facilities',
            name='gallery',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='facilities',
            name='liveScreening',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='facilities',
            name='locker',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='facilities',
            name='mobileCharging',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='facilities',
            name='parking',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='facilities',
            name='purifiedWater',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='facilities',
            name='shower',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='facilities',
            name='washRoom',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='turf',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='turf',
            name='gallery',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='turf',
            name='mapImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='turf',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='turf',
            name='review',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='turf',
            name='timePeriod',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='turf',
            name='sport',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='turf',
            name='turfName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
