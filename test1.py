import tushare as ts
import pandas as pd
# ts.set_token('7cd7736ea44951da2f48f0212b9084f1419db32a3b8908040256ed71')

pro= ts.pro_api('7cd7736ea44951da2f48f0212b9084f1419db32a3b8908040256ed71')

# stock_basic()获取所有，股票列表
Data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
print('获得上市股票总数：', len(Data)-1)

# 截取所有股票编号
# stocks=Data['ts_code']
# print(stocks)
# for i in list(stocks):
#     if i == '002371.SH':
#         print(i)
# j = 1
# for i in list(stocks):
#     # 1.通过股票编号i，ts.pro_bar()获取股票i前复权信息，时间2010~2021
#     data = ts.pro_bar(ts_code=i, adj='qfq', start_date='20100101', end_date='20211231')
 
#     # 2.保存数据
#     data.to_csv('/home/yys/python_lib/Toshare_work' + i + '.csv', index = False)
 
#     # 3.进度打印
#     print('正在获取第%d家，股票代码%s.' % (j, i))
#     j+=1

#  002371
i = '002371.SZ'
data = ts.pro_bar(ts_code=i, adj='qfq', start_date='20200101', end_date='20230422')
data.to_csv('/home/yys/python_lib/Toshare_work/002371/' + (i + '.csv'), index = False)
