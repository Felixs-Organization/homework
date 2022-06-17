import requests
import json
from lxml import etree
import time
#import pandas as pd
'''

    微博的300条评论 点赞 转发 主题 和 文章主要的文本



'''

url = "https://www.douyin.com/aweme/v1/web/module/feed/?device_platform=webapp&aid=6383&channel=channel_pc_web&module_id=7&count=4&filterGids=&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=2560&screen_height=1440&browser_language=en-US&browser_platform=MacIntel&browser_name=Firefox&browser_version=100.0&browser_online=true&engine_name=Gecko&engine_version=85.0&os_name=Mac+OS&os_version=10.13&cpu_core_num=4&device_memory=8&platform=PC&downlink=6.45&effective_type=4g&round_trip_time=100&webid=7100022480433153571&msToken=4BD2n9FW3HL3Dd5Y9--4n7dx0m6UMCr23TcJt3wTmGvxuZnN61nLu7Gu7tN3bNSix3fhv_lK2o_x_tPwrcpQYwfZF1A13IJuXFR08nih-gZUPwlUkaMJ0FTCHSIOCGbnKA==&X-Bogus=DFSzKwVOT4bANjUxS3nUTnlK58u0&_signature=_02B4Z6wo00001Q6lXOwAAIDC5.ddMXWyNyEOtVhAACEjod4IdHSBz9OyD6Z-IXW7iJpXHySLER6C-MMtxmMQlwHWrUOIZX8Uxt578WYjqvGs2j7izENtoGYKW2cESbAtfRwsFi.se7XSFIDPca"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:97.0) Gecko/20100101 Firefox/100.0",
    'cookie':'_zap=78c2bda7-9bd3-47f0-9a71-40dcd40bff8a; _xsrf=CDxZMcq2UOOcwkSv2trzEN6um4ZCqU7c; d_c0="AXBR164lIBSPTu-NGVAqW0FcQKWYAQfUvfk=|1638534745"; __snaker__id=rkbGfvcq7IVzyaJd; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=w8lO%2Fz6x3MlBFAUEBUNrsoUFYNFCeG4k; q_c1=14ca4a533ace4874b236d32bb5817dbd|1647745950000|1647745950000; captcha_ticket_v2=2|1:0|10:1651973755|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfQUZRNzlkUG9KSk43SlhlY191ejlNLXBiRVFlLXhYdWpKZFNkOEUuZkJxXzBpc3ppb1Z2RVZma3d4ZXhaV19PUUpjVG9SNFdPaFQ1aU9Bbm9wTkc5Wi1tTklPUTJ1NnZ6bHhWemg0MVE0dEVuQkw1bS4tQ09QeXhIT3Rmb3JoV3p5WjF3Ql8uYnNRNjhhbEVBNEQ3WmhUQkllNGdSWDV2QS5SR1NQdU4wS0ZvLjRkRGxWS0Z3UVRtcVdTZjRkaFpZOGFzZG1qeUo1VzlCQnNYMDk0RlVkdXNIVFhabHJJTXJVQVdJeHNfZmNOTkdTVldhWTdSTXRITklvU0NhX0suWno3dFlXdWx5d2tWWWFYeTJ4ZXNzMWZiOGtpN1FIMjdRRmZHNS5SZE9OdHBIU1Y4d0F2dHpTSl8yWXAtNF9xb3E0ajAuVGx2WHl4T1BKbXhJNWxOU1FZbVRZNW5uZjktelJYdlhLMkVhejVweFh3dUs0R2xMdHhGNGhYWVowNWZuOXJyWkc0bXNuZTFWLmdqVExLRkhEQUNhZzFSN0JUREloUmR1UjdVUXZ3aFoucVVRLWhULkgwdXJmLlFmQVNBeFRScUVjcG40Mkh3NXNSU3NvbVBXaGF1WGVQV2Q2ZFBXYmplQ0k3WlZtbVVlQnNsakF1bTZSWHY1di1TMyJ9|4b15b2124768ad4201c251eae5368eba93b8ed62c8b98416905e81d670610c20; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1651924380,1651972075,1652096465,1652496414; captcha_session_v2=2|1:0|10:1652496414|18:captcha_session_v2|88:NS9Bd1g1MS9YSk5YYng1VE93MkRLdFhLRWdnNlQwVTZnQ0R4V3FWZ1FyVXRrN1IwNFVaNXpLVVB6N2tlMWk4eg==|4d551de0f410cafebe587da0508dbab9e91e80c04610f1d1f3bc66c8851871d0; SESSIONID=X1Hap1MGrA5XP2voD0h6G564SsUndkbMKD8oaHyDN4i; JOID=Vl8XC0MonbHpnfQ6JiRiamE43RU0c6nziOHGcmtW34G7zcpPTDGKxIeS8jUs3EO9h8b38m0qlUV2kxhgoO8XWPU=; osd=UVsRAEMvmbfinfM-IC9ibWU-1hUzd6_4iObCdGBW2IW9xspISDeBxICW9D4s20e7jMbw9mshlUJylRNgp-sRU_U=; gdxidpyhxdE=O0nfUuhGsyKesrXKssdzG7011qPj1ZsKeAVa5Yxg2vzzyY2IjomoRym7pnI%2Bqwr2k%2Fte%5CRbj7lM8vz78%5CWa5wIdcEzeV17X%2FDsRkWlOjAf%2FbTl0xnXN%2Fgg%5CC%2BngR5XJVQKdUxqtOrWQHsnLum5yYqyJBPKAQAKS5to6CAVGL82cUsiSs%3A1652497316225; YD00517437729195%3AWM_NI=YY%2F78jlJDs8CY8q0HT6wFYF62l2qg%2FmSDIVSqF0KpXQ%2BMKIROM3B46CbO1SB%2BN%2BuBC8URKPwbps8%2BIEt61KI6dYJGN74xWmWGg5tiKBKpqYeV3leerEHfmiXv8Pfs89AbHM%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee8ec9418f9bbdd4e262b3a88eb7d45a879a9eb1c84aa69f8aace96da6e9a8a6ec2af0fea7c3b92a9b87e1d8bb62b0968c94bb499be8bfd1cb60f6a98abac53ef2b4fe92e625af8d8caad559b39a00acf35493f583accc5a8d93fda3b73e81be81d2d24ae992e596c149fc8b9eacd37da2b0bdd9aa4387acfad2ca43f6bc97abc646f5ecb8b8f05d85b9fb95ec418295c092dc6f96eda486e87a8798aa8eec54b6e8a087f234fb9faea9d037e2a3; o_act=login; ref_source=other_https://www.zhihu.com/signin?next=/; l_n_c=1; l_cap_id="NWU4MWRlNDBiOGJkNDM1ZDg5MDkxNDZlZmNiNTlmYzg=|1652496422|d2f16f66191ba9aef0932f536004cf11b90ec42c"; r_cap_id="YTQxNzUzM2Q0ZTNiNDY1ZjllNzc3ZWQzMzJjZWIxYmM=|1652496422|ad2f82d63889a5d4ca7b2b4ba10b1397b31c883e"; cap_id="NDliNDc2MmY4YTA4NDZlNDk4NmYzOTBlMDliNjhkNTY=|1652496422|e5afb08d248d64f1ec1f5c34b65f02a3da17f281"; n_c=1; expire_in=15552000; z_c0=2|1:0|10:1652496428|4:z_c0|92:Mi4xSll1aEhRQUFBQUFCY0ZIWHJpVWdGQmNBQUFCZ0FsVk5MR1pzWXdEbkRtRTViMHo1U3F1NzZ0dmVUZWdTZ1ZING93|5027947974c91929c316614bdf23f3bfe49e9e20b04d99e3eb98269e98a38d66; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1652496431; tst=r; NOT_UNREGISTER_WAITING=1; KLBRSID=ed2ad9934af8a1f80db52dcb08d13344|1652496468|1652496412',
}

time.sleep(0.5)
response = requests.get(url, headers=headers)
resp_json = response.json()
print("OK" if response.status_code == 200 else "Something weird happened")
print("writing resp_json to resp_json.json")


with open("./resp_json.json", "w") as f:
    json.dump(resp_json, f, indent=4)

'''
# attempt to find out how many times the post has been looked at / viewed
for i in range(6):
    print("----------{0}----------".format(i))
    print("views: ", resp_json["data"][i]["target"]["visited_count"])

    print("comments: ", resp_json["data"][i]["target"]["comment_count"])

    print("voteups: ", resp_json["data"][i]["target"]["voteup_count"])

    print("thanks: ", resp_json["data"][i]["target"]["thanks_count"])

    print("favorites: ", resp_json["data"][i]["target"]["favorite_count"])

lst = []

for i in resp_json['data']:

    f = {}

    f['favorite_count']=i['target']['favorite_count']

    f['comment_count'] = i["target"]["comment_count"]

    lst.append(f)

lst = []

lst = [{},{},{}]

# excel

print(lst)

data = pd.DataFrame(lst)

print(data)

data.to_excel('zhifu.xlsx')

'''