# Generated by Django 2.1 on 2018-08-15 09:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('til', '0002_auto_20180815_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 15, 9, 10, 38, 127255, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 15, 9, 10, 37, 862067, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 15, 9, 10, 38, 128256, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='til',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 15, 9, 10, 38, 127255, tzinfo=utc)),
        ),
    ]
