# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_auto_20160117_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourleads',
            name='expiry_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
