# Generated by Django 3.1.5 on 2021-03-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0055_coupon_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='used',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
