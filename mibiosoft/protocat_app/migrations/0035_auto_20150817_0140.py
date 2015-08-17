# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0034_auto_20150815_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('picture', models.ImageField(upload_to='')),
                ('biography', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='userregistration',
            name='first_name',
            field=models.CharField(max_length=20, default=''),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='last_name',
            field=models.CharField(max_length=20, default=''),
        ),
    ]
