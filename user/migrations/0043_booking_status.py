# Generated by Django 3.1.5 on 2021-02-16 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0042_auto_20210216_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(blank=True, default='pending', max_length=20, null=True),
        ),
    ]