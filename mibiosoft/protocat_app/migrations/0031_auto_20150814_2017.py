# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0030_protocol_date_of_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocol',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='protocol',
            name='protocol_type',
            field=models.CharField(max_length=2, choices=[('BC', 'Biochemistry'), ('BI', 'Bioinformatics'), ('BT', 'Botany'), ('CB', 'Cell Biology'), ('CH', 'Chemistry'), ('DB', 'Developmental Biology'), ('GN', 'Genetics'), ('IM', 'Immunology'), ('MB', 'Molecular Biology'), ('TC', 'Tissue Culture'), ('NA', 'Not Defined')], null=True, blank=True),
        ),
    ]
