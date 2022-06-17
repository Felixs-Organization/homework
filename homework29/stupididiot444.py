from time import time
import requests
import json
url='https://movie.douban.com/j/chart/top_list'
param={
    'type': '24',
    'interval_id': '100:90',
    'action':'', 
    'start': '0',#从库中的第几部电影去取
    'limit': '5',#一次取出的个数
    }
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 12; rv:97.0) Gecko/20100101 Firefox/97.0'
    }
'''
response=requests.get(url=url)
print(1)
'''
response=requests.get(url=url,params=param,headers=headers,timeout=30)
list_data=response.json()
with open('./douban.json','w',encoding='utf-8') as fp:
    json.dump(list_data,fp,ensure_ascii=False)

print('over!')