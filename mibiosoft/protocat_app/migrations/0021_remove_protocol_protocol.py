# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0020_protocol_user_rated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protocol',
            name='protocol',
        ),
    ]
