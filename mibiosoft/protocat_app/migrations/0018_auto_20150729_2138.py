# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0017_auto_20150717_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocol',
            name='num_ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='protocol',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
