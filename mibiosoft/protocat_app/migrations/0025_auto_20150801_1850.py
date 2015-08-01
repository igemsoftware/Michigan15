# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0024_protocol_protocol'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProtocolSteps',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('step', models.TextField(default='')),
            ],
        ),
        migrations.RenameField(
            model_name='protocol',
            old_name='protocol',
            new_name='protocol_steps',
        ),
    ]
