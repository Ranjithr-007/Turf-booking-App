# Generated by Django 3.1.5 on 2021-02-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_userdata_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turf',
            name='sport',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]