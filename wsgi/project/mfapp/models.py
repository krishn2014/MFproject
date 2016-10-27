from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50, blank=False)

class Fund(models.Model):
    name = models.CharField(max_length=50, blank=False)
    category = models.ForeignKey(Category)

class Scheme(models.Model):
    scheme_code = models.IntegerField(blank=False)
    isin_payout_growth = models.CharField(max_length=50, blank=True)
    isin_div_reinvestment = models.CharField(max_length=50, blank=True)
    scheme_name = models.CharField(max_length=100, blank=False)
    net_asset_value = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    repurchase_price = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    sale_price = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    date = models.CharField(max_length=50, blank=False)
    fund = models.ForeignKey(Fund)
