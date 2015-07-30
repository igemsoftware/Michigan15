# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0019_auto_20150730_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocol',
            name='user_rated',
            field=models.TextField(default=''),
        ),
    ]
