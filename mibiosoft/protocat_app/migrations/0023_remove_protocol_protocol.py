# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0022_protocol_protocol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protocol',
            name='protocol',
        ),
    ]
