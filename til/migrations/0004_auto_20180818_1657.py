# Generated by Django 2.1 on 2018-08-18 07:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('til', '0003_auto_20180815_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 18, 7, 57, 46, 360760, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 18, 7, 57, 46, 72054, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 18, 7, 57, 46, 362284, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='til',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 18, 7, 57, 46, 359759, tzinfo=utc)),
        ),
    ]
