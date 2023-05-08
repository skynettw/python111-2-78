from django.contrib import admin
from mysite import models        # 從 mysite 的資料夾中的 models.py 匯入所有的類別（資料表）

admin.site.register(models.HBicycleData)
admin.site.register(models.NKUSTnews)
admin.site.register(models.PhoneMaker)
admin.site.register(models.PhoneModel)
admin.site.register(models.StockInfo)

