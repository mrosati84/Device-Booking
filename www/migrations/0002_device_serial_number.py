# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='serial_number',
            field=models.CharField(default=b'H-ART 2015 XXXXXXXXXXX', max_length=50),
            preserve_default=True,
        ),
    ]
