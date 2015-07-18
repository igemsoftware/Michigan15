# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0013_protocol_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocol',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
