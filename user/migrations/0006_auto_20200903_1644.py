# Generated by Django 2.2.12 on 2020-09-03 16:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200811_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='membership_end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='membership_start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
