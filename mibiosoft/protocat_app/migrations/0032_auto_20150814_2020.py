# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0031_auto_20150814_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocol',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
