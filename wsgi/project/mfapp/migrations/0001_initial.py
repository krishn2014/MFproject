# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(to='mfapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scheme_code', models.IntegerField()),
                ('isin_payout_growth', models.CharField(max_length=50, blank=True)),
                ('isin_div_reinvestment', models.CharField(max_length=50, blank=True)),
                ('scheme_name', models.CharField(max_length=100)),
                ('net_asset_value', models.DecimalField(max_digits=9, decimal_places=4)),
                ('repurchase_price', models.DecimalField(max_digits=9, decimal_places=4)),
                ('sale_price', models.DecimalField(max_digits=9, decimal_places=4)),
                ('date', models.DateField()),
                ('fund', models.ForeignKey(to='mfapp.Fund')),
            ],
        ),
    ]
