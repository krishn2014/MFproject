# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mfapp', '0002_auto_20161027_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheme',
            name='net_asset_value',
            field=models.DecimalField(max_digits=9, decimal_places=4, blank=True),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='repurchase_price',
            field=models.DecimalField(max_digits=9, decimal_places=4, blank=True),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='sale_price',
            field=models.DecimalField(max_digits=9, decimal_places=4, blank=True),
        ),
    ]
