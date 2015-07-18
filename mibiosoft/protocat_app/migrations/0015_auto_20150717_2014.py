# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0014_protocol_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocol',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]
