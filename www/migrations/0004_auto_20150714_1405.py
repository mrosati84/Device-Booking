# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0003_auto_20150714_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='reserved_by',
            field=models.ForeignKey(default=False, to='www.User', null=True),
            preserve_default=True,
        ),
    ]
