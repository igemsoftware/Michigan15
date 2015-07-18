# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protocat_app', '0010_protocolupload_reagents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.TextField()),
                ('protocol_type', models.CharField(max_length=2, choices=[('BC', 'Biochemistry'), ('BI', 'Bioinformatics'), ('BT', 'Botany'), ('CB', 'Cell Biology'), ('CH', 'Chemistry'), ('DB', 'Developmental Biology'), ('GN', 'Genetics'), ('IM', 'Immunology'), ('MB', 'Molecular Biology'), ('TC', 'Tissue Culture'), ('NA', 'Not Defined')], null=True)),
                ('rating', models.DecimalField(max_digits=3, default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)], decimal_places=2)),
                ('reagents', models.TextField(default='')),
                ('protocol', models.TextField(default='')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ProtocolUpload',
        ),
    ]
