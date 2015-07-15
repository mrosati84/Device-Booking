# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0004_auto_20150714_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='reserved_by',
            field=models.ForeignKey(blank=True, to='www.User', null=True),
            preserve_default=True,
        ),
    ]
