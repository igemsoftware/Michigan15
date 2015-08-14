# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0029_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocol',
            name='date_of_upload',
            field=models.DateField(default=datetime.datetime(2015, 8, 14, 22, 48, 19, 587549, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
