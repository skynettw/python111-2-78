import os
import django
import requests                 #擷取網頁用的模組
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nkust1112web78.settings')
django.setup()
from mysite import models

models.StockInfo.objects.all().delete()
url = "https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_AVG_ALL"
r = requests.get(url).text
data = json.loads(r)
for d in data:
    try:
        rec = models.StockInfo(code=d['Code'], name=d['Name'],
                        price=float(d['ClosingPrice']),
                        mprice=float(d['MonthlyAveragePrice']))
        rec.save()
        print(d)
    except Exception as e:
        print(e)
        pass
    
print("Done")