# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0016_auto_20150717_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocol',
            name='rating',
            field=models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)], default=0.0, max_digits=3),
        ),
    ]
