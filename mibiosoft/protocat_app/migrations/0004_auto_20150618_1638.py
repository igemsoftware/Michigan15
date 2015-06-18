# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0003_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(null=True, max_length='50', default='Your Name'),
        ),
    ]
