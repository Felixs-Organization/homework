import requests
import pygal
import json
import pdb

headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:103.0) Gecko/20100101 Firefox/104.0" }
proxies = { 'http': 'http://127.0.0.1:53446', 'https': 'http://127.0.0.1:53446' }
url = "https://n.sinaimg.cn/default/7660da6d/20200426/world_geo.json"


response = requests.get(url, headers=headers, proxies=proxies)


print(response.text)






