from django.core.management.base import BaseCommand, CommandError
from mfapp.models import *
import re

exp_category = 'Schemes'
exp_mf = 'Mutual Fund'
exp_scheme = ';'

rip = lambda a: '' if a=='-' else a
rip_na = lambda a: None if a=='N.A.' else a

class Command(BaseCommand):
    help = 'Parses file and populates db with entries'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        file = options['file']
        category = None
        fund = None
        with open(file, 'r') as f:
            f.readline()
            for line in f.readlines():
                if not line.strip():
                    continue
                if re.search(exp_category, line):
                    category, created = Category.objects.get_or_create(category=line.strip())
                elif re.search(exp_mf, line):
                    if category is None:
                        raise Exception ("Files is in wrong format")
                    fund, created = Fund.objects.get_or_create(name=line.strip(), category=category)
                elif re.search(exp_scheme, line):
                    if fund is None:
                        raise Exception ("Files is in wrong format")
                    items = map(rip, line.strip().split(';'))
                    items = map(rip_na, items)
                    scheme, created = Scheme.objects.get_or_create(scheme_code=items[0], isin_payout_growth=items[1], isin_div_reinvestment=items[2], scheme_name=items[3], net_asset_value=items[4], repurchase_price=items[5], sale_price=items[6], date=items[7], fund=fund)
                else:
                    raise Exception ("Unknown string found: %s" % line)
        print "database populated successfully"
