# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0015_auto_20150717_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocol',
            name='rating',
            field=models.DecimalField(max_digits=3, decimal_places=2, default=1.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
