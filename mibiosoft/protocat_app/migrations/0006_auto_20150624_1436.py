# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0005_userregistration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protocol',
            name='author',
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='full_name',
            field=models.CharField(max_length=50, null=True, default='Your Name'),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Protocol',
        ),
    ]
