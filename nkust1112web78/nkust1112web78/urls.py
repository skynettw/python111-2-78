from django.contrib import admin
from django.urls import path
from mysite import views     # 從views.py去匯入所有的處理函式

urlpatterns = [
    path('news/', views.nkustnews),
    path('phonelist/', views.phonelist),  # 列出所有新款手機
    path('phonelist/maker/<int:id>/', views.phonelist),  # 列出指定廠牌的所有手機
    path('stock300list/', views.stock300list), # 列出所有股價超過300元的公司
    path('chart/', views.chart), 
    path('all/', views.all_data),         # 顯示所有的站
    path("filter/", views.filtered_data), # 顯示超過10台可用自行車的站
    path('', views.index ),  # 如果有人來瀏覽首頁的話，請交給views.py裡面的index()函式處理
    path('admin/', admin.site.urls),
]
