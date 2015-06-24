# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0006_auto_20150624_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuthentication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='YourUserName', max_length=50)),
                ('password', models.TextField(default='password123', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='updated',
        ),
        migrations.AddField(
            model_name='userregistration',
            name='password',
            field=models.TextField(default='password123', max_length=20),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='user_name',
            field=models.CharField(default='YourName', max_length=50),
        ),
    ]
