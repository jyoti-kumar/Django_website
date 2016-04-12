# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panilty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qno', models.CharField(max_length=30)),
                ('panilty', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='submission',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 4, 21, 50, 1, 44841)),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='panilty',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='panilty',
            field=models.ManyToManyField(to='home.Panilty'),
        ),
    ]
