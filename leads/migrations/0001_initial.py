# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TourLeads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(default=b'm', max_length=1, choices=[(b'm', b'Male'), (b'f', b'Female')])),
                ('card_number', models.CharField(max_length=15, null=True, blank=True)),
                ('expiry_date', models.DateField(null=True, blank=True)),
                ('professional', models.CharField(default=b'y', max_length=1, choices=[(b'y', b'Yes'), (b'n', b'No')])),
            ],
        ),
        migrations.CreateModel(
            name='TourLeadsLanguages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.ForeignKey(to='leads.Languages')),
                ('tourlead', models.ForeignKey(to='leads.TourLeads')),
            ],
        ),
        migrations.AddField(
            model_name='tourleads',
            name='languages',
            field=models.ManyToManyField(to='leads.Languages', through='leads.TourLeadsLanguages'),
        ),
    ]
