# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourleads',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 22, 10, 53, 804000, tzinfo=utc)),
        ),
    ]
