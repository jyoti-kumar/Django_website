# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question_ans_key',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('q_no', models.CharField(max_length=30)),
                ('ans', models.CharField(max_length=30)),
                ('key', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 11, 2, 20, 22, 46, 66527))),
                ('qno', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, serialize=False, primary_key=True)),
                ('website', models.URLField(blank=True)),
                ('current_q_no', models.CharField(default=b'1', max_length=30)),
                ('panilty', models.CharField(default=b'0', max_length=30)),
                ('lst', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(to='home.UserProfile'),
        ),
    ]
