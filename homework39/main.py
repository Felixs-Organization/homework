#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import requests
from rich import print as pprint
import json

proxies = {
    'http': 'http://127.0.0.1:53446',
    'https': 'http://127.0.0.1:53446',
}

proxies_burp = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}


# URL
url = "https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=2c0830ea97de1d74be94529a743cc6f7&desktop=true&page_number=2&limit=6&action=down&after_id=5&ad_interval=-10"


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Cookie': '_xsrf=t4Kp8rz5YNLp1NBL6YegdTxDDfSOPNcz; _zap=823635f3-6300-4891-9e4f-76f84b65528d; d_c0="ABBeeM8q8BSPTrAWUHzNM6DO58_QpH5Js48=|1652494733"; KLBRSID=57358d62405ef24305120316801fd92a|1657940548|1657939454; captcha_session_v2=2|1:0|10:1657939457|18:captcha_session_v2|88:SUxBU1NLWFpIaGZYNUpJU05Vc0hFL1hFdGhsU0ZxK1VWL2duSFZZaVZBbHNTNHR1TllxQ0tKWXltOTNOTnBXMw==|ceb39c2eb6a75e7ba3329dfe69a9422c5979d8b0962929b86a8b6e220a10bab6; SESSIONID=eU4VVVYLv7d4G2dg5l8IdhBNT58D1pZpfqPWLlp3oHQ; __snaker__id=manWJdzzW2FuxqqS; gdxidpyhxdE=R%5C8EAGO6mUshRalk3v%5C9RLIrmHgUYNEwqzDSOaZiRH4ByCfoQ4SQBA6IuaVOjPhqukQ%5CUPN1zwghAQ9bN%5CI85hVc3H%2FMZaqogT%2B2pDlwe2Ck0nJWXsmuLi%2Fibd3AaQAMP6%2FZMyUJeox0yobriU15DMO52OBb%2BxmB56vTBbpsj%2FnWUcWD%3A1657940368258; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=z3eHFpmHm4SHwn6BfYrIuju4qfy%2F1GD%2BneqNPukhQTo%2BpHTunndwSf1qLqfrSOk4sLAr%2BaoERrPjWPakQLcYNn7ILNhxhhXVQ9FerTPkR3N6E5Maml7FCXtPyYUOePlzVWs%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea6bc25f4eda799cb41a1eb8fa6c54e878e9ab0d85d838ba993c6548ab0b694b52af0fea7c3b92abaedaba9c57caf98a3d5d244b5b2faa3e553b297bb8bf840b3bab7d0b44d88f5a286f44694aba589d460adf5c0a9d77faeb2ac98d26ef3af8492e57a9191a5d5f24883aee582ee4f92aea08bd65ca3b59fade2538eb2f9aacf46aca8a889db5e93e78a86f16094b59ed4cd3e87eb8382f068f59a8db9f75cbb879bb0e85cb0a69ab8f237e2a3; YD00517437729195%3AWM_TID=T3VzZ2lh%2F5pEUEFBABKATQRhuXXJo3tq; o_act=login; ref_source=other_https://www.zhihu.com/signin?next=/; expire_in=15552000; z_c0=2|1:0|10:1657939481|4:z_c0|92:Mi4xSll1aEhRQUFBQUFBRUY1NHp5cndGQmNBQUFCZ0FsVk5HWFNfWXdBQmRhZEJXaHVtVjZJVkVhNjY0bUQ0ZC1vdFV3|1c6c46cd0d0ba3231a236036e1f588359d628ac0f22951047090656e2a408d73; q_c1=48d2dbe3ef0141ca97d19992b1dda647|1657939482000|1657939482000; NOT_UNREGISTER_WAITING=1; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1657939569; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1657940546; JOID=VlASCkOR0GJ63SgvJZxQPkrqaG4z-IpYLYdyeWfr6wlAmxZHTdH7vxXdKy4q_KvA_xz8UM-M1C-52S6tdxD-oqM=; osd=UlwWB0KV3GZ33CwjIZFROkbuZW839I5VLIN-fWrq7wVElhdDQdX2vhHRLyMr-KfE8h34XMuB1Su13SOscxz6r6I=; tst=r'
}

response = requests.get(url=url, headers=headers)
resp_json = response.json()


pprint("[grey][-] Proxy: {}[/]".format(proxies['http']))
pprint("[green][+] 200 OK[/]" if response.status_code == 200 else "[red][-] {}[/]".format(response.status_code))        


pprint("[grey][-] Writing resp_json.json...[/]")

with open("resp_json.json", "w") as f:
    json.dump(resp_json, f, indent=4)

pprint("[grey][-] Printing out the headline...[/]")
pprint()