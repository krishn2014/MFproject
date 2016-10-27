# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mfapp', '0003_auto_20161027_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheme',
            name='net_asset_value',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='repurchase_price',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='sale_price',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=4),
        ),
    ]
