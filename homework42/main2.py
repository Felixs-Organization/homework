import requests
import json

proxies = {
        'http': 'http://127.0.0.1:53446',
        'https': 'http://127.0.0.1:53446'
}


url = 'http://stockpage.10jqka.com.cn/spService/600519/Funds/realFunds/free/1/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:103.0) Gecko/20100101 Firefox/103.0'
}



response = requests.get(url, proxies=proxies, headers=headers)
resp_json = response.json

print("ok" if response.status_code == 200 else 'not ok')

with open('resp.json', 'w') as f:
    f.write(resp_json)
