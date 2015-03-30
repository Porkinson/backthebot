# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150329_2156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='away_score',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text_away',
            new_name='home_score',
        ),
    ]
