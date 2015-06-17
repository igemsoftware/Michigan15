# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('protocat_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='protocol',
            name='protocol',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='protocol',
            name='protocol_type',
            field=models.CharField(max_length=2, choices=[('BC', 'Biochemistry'), ('BI', 'Bioinformatics'), ('BT', 'Botany'), ('CB', 'Cell Biology'), ('CH', 'Chemistry'), ('DB', 'Developmental Biology'), ('GN', 'Genetics'), ('IM', 'Immunology'), ('MB', 'Molecular Biology'), ('TC', 'Tissue Culture')], null=True),
        ),
        migrations.AddField(
            model_name='protocol',
            name='rating',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)], decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.RemoveField(
            model_name='protocol',
            name='author',
        ),
        migrations.AddField(
            model_name='protocol',
            name='author',
            field=models.ManyToManyField(to='protocat_app.Author'),
        ),
    ]
