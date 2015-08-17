# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0038_userprofile_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='biography',
            field=models.TextField(default='Protocat'),
        ),
    ]
