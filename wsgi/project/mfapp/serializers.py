from rest_framework import serializers

# importing models
from models import *

class SchemeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheme
        fields = ['scheme_code', 'isin_payout_growth', 'isin_div_reinvestment', 'scheme_name', 'net_asset_value', 'repurchase_price', 'sale_price', 'date']

class SchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheme
        fields = ['scheme_code', 'scheme_name', 'net_asset_value',]
