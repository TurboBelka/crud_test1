# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20160117_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourleads',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 16, 22, 16, 21, 87000, tzinfo=utc)),
        ),
    ]
