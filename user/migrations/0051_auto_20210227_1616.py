# Generated by Django 3.1.5 on 2021-02-27 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0050_booking_ttpe_of_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='ttpe_of_booking',
            new_name='type_of_booking',
        ),
    ]