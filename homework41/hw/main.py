import pygal
import requests
import json


url = "http://stockpage.10jqka.com.cn/spService/600519/Funds/realFunds/free/1/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Cookie": "v=A34sfRdTkSlMKcUNE1oUXEgJyZXFv0I51IP2HSiH6kG8yxLBkE-SSaQTRi77; historystock=600519; spversion=20130314"
}


response = requests.get(url, headers=headers)
resp_json = json.dumps(response.json())
print("[+] made request successfully")

print("[*] writing to file")

with open("resp.json", "w") as f:
    f.write(json.dumps(response.json(), indent=4))

print("[+] wrote to file resp.json")


print('[*] parsing json')

# ddje, sr, hyje, je
je = dict()
ddje = dict()
sr = dict()
hyje = dict()

for i in resp_json["flash"]:
    sr["name"] = i["sr"]

hyje[resp_json["field"]["hyname"]] = resp_json["field"["hyje"]]

for i in resp_json["field"]["hyzdf"]:
    je["stockname"] = i["je"]

for i in resp_json["desc"]:
    ddje["stockname"] = i["ddje"]


print("[*] writing all to file called all.json")

al = [je, ddje, sr, hyje]

with open("all.json", "w") as f:
    f.write(json.dumps(al, indent=4))

# 茅台的价格做成折线图
