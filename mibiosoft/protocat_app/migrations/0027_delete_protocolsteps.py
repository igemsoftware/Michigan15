# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0026_auto_20150801_1920'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProtocolSteps',
        ),
    ]
