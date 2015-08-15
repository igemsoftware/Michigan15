# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0032_auto_20150814_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocol',
            name='date_modified',
            field=models.DateField(auto_now=True, default=datetime.datetime(2015, 8, 15, 16, 41, 0, 716861, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
