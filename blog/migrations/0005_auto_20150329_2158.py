# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150329_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='away_score',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='home_score',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
