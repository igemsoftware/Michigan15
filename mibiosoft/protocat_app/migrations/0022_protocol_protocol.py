# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0021_remove_protocol_protocol'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocol',
            name='protocol',
            field=models.TextField(default=''),
        ),
    ]
