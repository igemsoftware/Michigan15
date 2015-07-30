# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0018_auto_20150729_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocol',
            name='rating',
            field=models.DecimalField(max_digits=3, default=2.5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)], decimal_places=2),
        ),
    ]
