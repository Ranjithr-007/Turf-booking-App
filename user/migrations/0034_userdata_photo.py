# Generated by Django 3.1.5 on 2021-02-13 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0033_auto_20210212_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
