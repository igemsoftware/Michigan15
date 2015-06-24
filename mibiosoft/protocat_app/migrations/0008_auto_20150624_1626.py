# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0007_auto_20150624_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userauthentication',
            name='password',
            field=models.CharField(default='password123', max_length=120),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='password',
            field=models.CharField(default='password123', max_length=120),
        ),
    ]
