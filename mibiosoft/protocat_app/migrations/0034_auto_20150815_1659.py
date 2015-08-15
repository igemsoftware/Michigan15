# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0033_protocol_date_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocol',
            name='date_of_upload',
            field=models.DateField(auto_now_add=True),
        ),
    ]
