# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150329_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='away_score',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='home_score',
            new_name='text_away',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='home',
            new_name='title',
        ),
    ]
