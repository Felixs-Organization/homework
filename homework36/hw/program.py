import requests


url = 'https://www.kugou.com/yy/html/rank.html'
headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:101.0) Gecko/20100101 Firefox/101.0'
    }


response = requests.get(url, headers=headers)

status_code = response.status_code

print("OK" if status_code == 200 else "NOT OK")
