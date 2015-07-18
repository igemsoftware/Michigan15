# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protocat_app', '0012_remove_protocol_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocol',
            name='author',
            field=models.ForeignKey(default='', to=settings.AUTH_USER_MODEL),
        ),
    ]
