# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20160308_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 13, 0, 23, 53, 353422)),
        ),
    ]
