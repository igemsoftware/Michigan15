# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0025_auto_20150801_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userauthentication',
            name='password',
            field=models.CharField(default='password', max_length=120),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='password',
            field=models.CharField(default='password', max_length=120),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='user_name',
            field=models.CharField(default='First Last', max_length=50),
        ),
    ]
