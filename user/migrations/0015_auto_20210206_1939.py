# Generated by Django 3.1.5 on 2021-02-06 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20210205_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='paymentOption',
            new_name='payment_option',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='turf',
        ),
        migrations.AddField(
            model_name='booking',
            name='sport',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='time_period',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='turf_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='userdata',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.userdata'),
        ),
    ]
