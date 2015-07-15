# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_device_serial_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='device',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='user',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.RemoveField(
            model_name='device',
            name='available',
        ),
        migrations.AddField(
            model_name='device',
            name='reserved_by',
            field=models.ForeignKey(default=False, to='www.User'),
            preserve_default=True,
        ),
    ]
