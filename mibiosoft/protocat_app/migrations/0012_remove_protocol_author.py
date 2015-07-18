# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0011_auto_20150717_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protocol',
            name='author',
        ),
    ]
