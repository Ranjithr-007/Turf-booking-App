# Generated by Django 3.1.5 on 2021-02-09 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0004_delete_users'),
        ('user', '0018_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turf',
            name='facilities',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admins.facilities'),
        ),
        migrations.AlterField(
            model_name='turf',
            name='sport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admins.category'),
        ),
    ]