import requests


proxies = {
    'http': 'http://127.0.0.1:53446',
    'https': 'http://127.0.0.1:53446'
}

url = 'https://www.nm.zsks.cn/22gkwb/gktj_22_41_20/data/tjyx.json' # ?path=A,B,C,D,E
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:103.0) Gecko/20100101 Firefox/103.0'
}

response = requests.get(url, headers=headers, proxies=proxies)

print('[+] Sucessful GET request' if response.status_code == 200 else '[-] Unsuccessful GET request')   
