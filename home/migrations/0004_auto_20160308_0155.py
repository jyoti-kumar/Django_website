# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20151104_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 8, 1, 55, 14, 677991)),
        ),
    ]
