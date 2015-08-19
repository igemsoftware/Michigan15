# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0039_auto_20150817_1250'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
