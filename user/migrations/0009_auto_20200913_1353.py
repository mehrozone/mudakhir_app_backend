# Generated by Django 2.2.12 on 2020-09-13 13:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20200913_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sallaryDate',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
