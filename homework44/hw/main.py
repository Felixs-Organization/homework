import requests

url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=c6c1362415c37d0167506d3e9ed1d066&desktop=true&page_number=4&limit=6&action=down&after_id=17&ad_interval=-10'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'cookie':'_zap=78c2bda7-9bd3-47f0-9a71-40dcd40bff8a; _xsrf=CDxZMcq2UOOcwkSv2trzEN6um4ZCqU7c; d_c0="AXBR164lIBSPTu-NGVAqW0FcQKWYAQfUvfk=|1638534745"; __snaker__id=rkbGfvcq7IVzyaJd; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=w8lO%2Fz6x3MlBFAUEBUNrsoUFYNFCeG4k; q_c1=14ca4a533ace4874b236d32bb5817dbd|1647745950000|1647745950000; gdxidpyhxdE=O0nfUuhGsyKesrXKssdzG7011qPj1ZsKeAVa5Yxg2vzzyY2IjomoRym7pnI%2Bqwr2k%2Fte%5CRbj7lM8vz78%5CWa5wIdcEzeV17X%2FDsRkWlOjAf%2FbTl0xnXN%2Fgg%5CC%2BngR5XJVQKdUxqtOrWQHsnLum5yYqyJBPKAQAKS5to6CAVGL82cUsiSs%3A1652497316225; YD00517437729195%3AWM_NI=YY%2F78jlJDs8CY8q0HT6wFYF62l2qg%2FmSDIVSqF0KpXQ%2BMKIROM3B46CbO1SB%2BN%2BuBC8URKPwbps8%2BIEt61KI6dYJGN74xWmWGg5tiKBKpqYeV3leerEHfmiXv8Pfs89AbHM%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee8ec9418f9bbdd4e262b3a88eb7d45a879a9eb1c84aa69f8aace96da6e9a8a6ec2af0fea7c3b92a9b87e1d8bb62b0968c94bb499be8bfd1cb60f6a98abac53ef2b4fe92e625af8d8caad559b39a00acf35493f583accc5a8d93fda3b73e81be81d2d24ae992e596c149fc8b9eacd37da2b0bdd9aa4387acfad2ca43f6bc97abc646f5ecb8b8f05d85b9fb95ec418295c092dc6f96eda486e87a8798aa8eec54b6e8a087f234fb9faea9d037e2a3; z_c0=2|1:0|10:1652496428|4:z_c0|92:Mi4xSll1aEhRQUFBQUFCY0ZIWHJpVWdGQmNBQUFCZ0FsVk5MR1pzWXdEbkRtRTViMHo1U3F1NzZ0dmVUZWdTZ1ZING93|5027947974c91929c316614bdf23f3bfe49e9e20b04d99e3eb98269e98a38d66; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1659608451,1659748778,1662027962,1662173791; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1662173791; tst=r; NOT_UNREGISTER_WAITING=1; BAIDU_SSP_lcr=https://www.baidu.com/link?url=KSNDPajtwWs42t0COydAUlKkJ0gP-yExzWlPY39d8q7&wd=&eqid=d18e343a008c92a9000000026312c25b; SESSIONID=qR5Xx9Djvz4qZTxGqesb47sPFAhPtlRhy8NhzhdvOKy; JOID=VFAcB0zgkU78lrLiEuJunHc3lc0Jn8J2p--Fp3WX5XuAz-eUVItfUp2Zve4cZ9QkvGVLj0agSZyu4OSzjehaVGE=; osd=VlAQAULikUL6mLDiHuRgnnc7k8MLn85wqe2Fq3OZ53uMyemWVIdZXJ-ZsegSZdQoumtJj0qmR56u7OK9j-hWUm8=; KLBRSID=0a401b23e8a71b70de2f4b37f5b4e379|1662173862|1662173789'
}

proxies = {
    'http': 'http://127.0.0.1:53446',
    'https': 'http://127.0.0.1:53446'
}



con = requests.get(url,headers=headers).json()
# print(con)
e = []
d = []
for i in con['data']:
    print(i['target']['id'])
    print('https://www.zhihu.com/api/v4/comment_v5/answers/'+str(i['target']['id'])+'/root_comment?order_by=score&limit=20&offset=')
    e.append('https://www.zhihu.com/api/v4/comment_v5/answers/'+str(i['target']['id'])+'/root_comment?order_by=score&limit=20&offset=')


for url in e:
    response = __import__("requests").get(url, headers=headers, proxies=proxies).json()
    for j in response["data"]:
        d.append(j["content"])



with open('d.txt', 'w') as _:
   for frv in d:
        _.write(frv)
        _.write("\n")

print("done")