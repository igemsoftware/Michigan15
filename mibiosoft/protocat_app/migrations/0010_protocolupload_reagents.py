# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0009_protocolupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocolupload',
            name='reagents',
            field=models.TextField(default=''),
        ),
    ]
