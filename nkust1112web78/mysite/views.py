from django.shortcuts import render   # 渲染網頁
from django.http import HttpResponse   # Django用來回應給瀏覽器特定資料的函式
import requests   # 匯入擷取網頁所需要的模組
import json       # 匯入操作JSON格式所需要的模組

def index(request):
    myname = "高雄金城武"
    return render(request, "index.html", locals())

def all_data(request):
    url = "https://opendata.hccg.gov.tw/OpenDataFileHit.ashx?ID=48DEDBDAC3A31FC6&u=77DFE16E459DFCE3F5CEA2F931E333F7E23D5729EF83D5F20744125E844FB27044F9892E6F09372518441B3BB84260426ADE242A57DFB9E8C9A50C50134F4F47"

    r = requests.get(url)         
    data = json.loads(r.text)     
    msg = ""
    msg = "<h2>新竹市自行車可用資訊" + data['updated_at'] + "</h2><hr>"   
    bicycle_data = data['retVal'] 
    msg = msg + "<table><tr bgcolor=#aaaaaa><td>站名</td><td>可用數量</td></tr>"
    for item in bicycle_data:
        msg = msg + "<tr bgcolor=#33ff33><td>{}</td><td>{}/{}</td></tr>".format(item['sna'].split("_")[1], item['sbi'], item['tot'])
    msg = msg + "</table>"
    return HttpResponse(msg)

def filtered_data(request):
    return render(request, "filter.html", locals())
