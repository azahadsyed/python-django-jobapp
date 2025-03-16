# Generated by Django 5.1.6 on 2025-03-09 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newjobpost',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2025, 3, 9, 17, 44, 15, 785885, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newjobpost',
            name='description',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newjobpost',
            name='salary',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
