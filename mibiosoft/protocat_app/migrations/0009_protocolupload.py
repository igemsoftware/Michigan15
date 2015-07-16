# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0008_auto_20150624_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProtocolUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('protocol_type', models.CharField(null=True, max_length=2, choices=[('BC', 'Biochemistry'), ('BI', 'Bioinformatics'), ('BT', 'Botany'), ('CB', 'Cell Biology'), ('CH', 'Chemistry'), ('DB', 'Developmental Biology'), ('GN', 'Genetics'), ('IM', 'Immunology'), ('MB', 'Molecular Biology'), ('TC', 'Tissue Culture'), ('NA', 'Not Defined')])),
                ('rating', models.DecimalField(default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)], decimal_places=2)),
                ('protocol', models.TextField(default='')),
            ],
        ),
    ]
