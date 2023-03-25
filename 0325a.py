import requests   # 匯入擷取網頁所需要的模組
import json       # 匯入操作JSON格式所需要的模組
url = "https://opendata.hccg.gov.tw/OpenDataFileHit.ashx?ID=48DEDBDAC3A31FC6&u=77DFE16E459DFCE3F5CEA2F931E333F7E23D5729EF83D5F20744125E844FB27044F9892E6F09372518441B3BB84260426ADE242A57DFB9E8C9A50C50134F4F47"

r = requests.get(url)         # 實際擷取網頁的內容
data = json.loads(r.text)     # 把網頁的文字轉換成JSON格式，放到data變數裡面
print(data['updated_at'])     # 印出指定欄位的內容 data是字典格式
bicycle_data = data['retVal'] # bicycle_data現在是串列格式，目前共有70筆項目
for item in bicycle_data:
    print("{}:{}/{}".format(
        item['sna'].split("_")[1], 
        item['sbi'], 
        item['tot']))
