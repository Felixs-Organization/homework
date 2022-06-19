import requests
import json
import os

url = 'https://haokan.baidu.com/web/video/feed?tab=recommend&act=pcFeed&pd=pc&num=30&shuaxin_id=1655574503671'

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12.00; rv:101.0) Gecko/20100101 Firefox/101.0'
    }


print("Sending Request...")
response = requests.get(url, headers=headers)

print("200 OK" if response.status_code == 200 else "NOT OK")

if response.status_code != 200:
    exit(1)


resp_json = response.json()

print("Writing resp.json...")

with open('resp.json', 'w') as resp_jsonf:
    f.write(json.dumps(resp_json))


if not o
