# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20151104_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 4, 21, 58, 25, 101262)),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='panilty',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='panilty',
            field=models.CharField(default=b'0', max_length=30),
        ),
        migrations.DeleteModel(
            name='Panilty',
        ),
    ]
