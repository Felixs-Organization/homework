import requests
import json


url = 'https://fanyi.baidu.com/sug'
what2translate = input('input what you want to translate: ')
print('using baidu translate to translate %s to Chinese' % what2translate)


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:96.0) Gecko/20100101 Firefox/96.0"
}

data3 = {
    'kw': what2translate
}

response = requests.post(url=url, data=data3, headers=headers)
re_js = response.json()
fn = "./json/%s_translate_results.json" % what2translate

with open(fn, 'w', encoding='utf-8') as file:
    json.dump(re_js, file, ensure_ascii=False)