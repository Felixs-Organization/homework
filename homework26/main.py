#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from lxml import etree





def dictcookies(cookiestext):
	cookies = {}
	cookiespure = cookiestext.replace(' ','')
	cookieslist = cookiespure.split(';')
	for i in cookieslist:
		key,value = i.split('=',1)
		cookies[key] = value
	return cookies



cook1es = "DefaultAnchorMailbox=0003BFFD15E74107@84df9e7f-e9f6-40af-b435-aaaaaaaaaaaa; O365Consumer=1; SuiteServiceProxyKey=rTiu94Uro3XWCr2N0NinI8EvqWPCBYGJWxJbGGH/IAA=&SjP6bLd8gxIh86VlCcPmqg==; X-OWA-CANARY=d2tekWscTESTL0haQ4U_8iAULAMf09kYrFZGjHAkM9TH5gFE_QfWetcbwLvex_8k9Igpe7V6KY4.; MicrosoftApplicationsTelemetryDeviceId=fc57e797-75fc-4ff2-9567-85552828a1be; MicrosoftApplicationsTelemetryFirstLaunchTime=2022-01-09T03:10:39.905Z; ClientId=591B5B02C19C4FBBB6F6047AD6F24757; MSFPC=GUID=a241848e20b6475c97f22558fea385b5&HASH=a241&LV=202102&V=4&LU=1613686611795; wlidperf=FR=L&ST=1641602642619; MUID=27AA69F382A968453F816611832D69FA; NAP=V=1.9&E=19ee&C=hwTJm2gQTjm1h1ktbFg27umq8HWmfBx2tIKJ2gCB11fBE38LnVOB4Q&W=1; ANON=A=286475ACFC8D5BE24F56B30EFFFFFFFF&E=19df&W=1; mkt=en-US; PPLState=1; MSPAuth=3fR2WNS*mAbe6zHk1MMFQN!B4SG!*D7*LCAV!JgP!!dskr1p0NTdHTiLmA5eMWmPqZojvKa5HiQ6BG!30NZTnvHcgaJ8yvLPCEDhwmbbIK4vsQeuAbHZetfvnentcnemuGyiBKY2eBb5A$; MSPProf=3mhFXVUxxBB*EfH5TZlWwm8n8ZfBtMj7w3Rk6b2VNnvnYWuj4dfYR1R0Ymtoh2k3vYFpSwzvd6I31fCVKXKyidtxHtWsRQklZBkUazH2bTee!eEba5I1wtkDG0!KYNTe2PW3q2jiLHAFECA3A*IFQOhjjG8RSxORSMWuPVwDwqkH8jobW0cvJ4DTiYUd8J8Q**; WLSSC=EgAhAgMAAAAMgAAADQABALxNBb6PdKHoe5KXGHB6mXiHJQz5/rIKWM8x5QZZCdB374Azc0oEP2qRY05IHk94P980CQswv/OlCO6QuBGLVBm++RGW8SDW33DS/GHcQU+JgAU9wqQEMn0evr+KIR3TXAL6A8jfT5oYXiV19dL074CHPBLi2ysEKRnGeuyF/ZAfegY5j43nsgo5H+/ZIScpmkLLD+kJrMhpmSo2t8DVhRzKTw83y/HgIdaS5S3/qXbY6o05hYVqkwy5fz8WNvrqhE1CVBgs8Vl2tdVO/FlskwIlaOKtavftUeQFbVlgFSg0pF37zqlTlUTa1M/sCXM0y4xgSypHrOfBnJ1wYN97HhABewAQAf2/AwAHQecVtVDaYVLe2GEQJwAAChCgABAVAGZlbGl4Y291QG91dGxvb2suY29tAFYAACFmZWxpeGNvdSVvdXRsb29rLmNvbUBwYXNzcG9ydC5jb20AAAUVVVMAAAAAAAAECQIAAHHpVVAABkMABUZlbGl4AAJPdQAAAAAAAAAAAAAAAAAAAAAAAIKJ/C2exkuBAAC1UNphNaLbYQAAAAAAAAAAAAAAAA8AMjQuMTMwLjE2Mi4xMDcABQIAAAAAAAAAAAAAAAAQBAAAAAAAAAAAAAAAAAAAAN5Lx7j4gnR/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/z8jAMhwQYUAAAAAAwI=; RPSAuth=FAB2ARQOIsqiBiVNmgLUgB%2B8kqQxgfQu%2BA5mAAAMgAAAEEqfQW99TN1Iu5wCEQ5JjxkgAZqcDWZERMttaMrOtV70TqPajLZ5XQ7XaYrvIjG909tvTyJbUnrttyec1zmvoDtteYa8XP8VT4Lfhlw3GxgB73eqkb1NlFcPJMnRA70qF6dSdFXJhrQW8uNvILbwloIl6Z6foLh/qSEXnLycIL4qpWO406z85aF1nVXylihoyqCS1gJ7D8%2B9Cohz6Mrg2J7BHrvM93IauD7DjTTcpfLWGFZRnYM4c94IoWMfUJNwOKg3ZQl4XX2SwPVQmq3Gxky98pQa/3LwDG9LkGA6Ljew5UHVmvEEK/Bxp5W0KXd1IaxYpRojQABefbt6OrZSksqzLcNyP/CfsGVT6tt0vrTgjfp60dRYNmenFwiMJEDYPv6EoJiuvtICfGnMzKUlrdamdiAA/T7yPmnIG5ToWDSDNvgN9QhxpNviINDI94%2BA1Vz8n8k%3D; RPSSecAuth=FAB2ARQOIsqiBiVNmgLUgB%2B8kqQxgfQu%2BA5mAAAMgAAAEEuapCWxnL4GvS3M9Gd5uxUgATyb5GHg8TnoHxFTIP8A0dIayE0dvqHZaNx/A2NGo/pgd5hqVgsQEl/pAj0NgesIOEAjP5G6KQfWdeb%2BaD/sF6OdWnv/j9DhJoR0BPofX2trVx5VcaQ8tliQwaTMJIwk/uLe27xEnZq973aiXFm0pU8YrZByFLtifmhcXZs/cuZnm2JmdQCaYsAdI8Urs2iFDWD0QBTeRspKplBxYnX8DSATRwZaHul3Ms6TVqqK591RTNXvZMg1pAogNYQwTQ2LW/dVZbFWVXBSi9gdWIA9WcWXQIDZA7LRfjB%2BcqwTH1NpuzuPMDLJlfAAd2xS2KKzJOwUF3jAlYSCPHvtNnE6xaIlyHJLKzKdmU1V9tJiEiobkRb%2BTXk8xm99%2BS/ReI8lHCAA3fKSW0Z5qR6HPMmZCAyPvWW2C40PLhpPrBdK226axUg%3D; MH=MSFT; OptInH=1P3SLHpjojwsRebEHHR_W7jLbPFMJMmB1fLbBFnUjsg; RoutingKeyCookie=v2:rgtBOdbjfK5rVNg5DsWPLm0%2f%2brndQTTThhCu6X8wmW0%3d:0003bffd-15e7-4107-0000-000000000000@outlook.com; UC=946e9802163f4e2ba812e21b8e70d2da; exchangecookie=3513fb77d21a4388aad122002ed1acd8; RpsCsrfState.dgWBHlEo9ore1VhI_M54E0sd3pL1A93A-6dFpwBh2bQ=315661b4-d38c-a749-ebbc-51f816614b45; X-OWA-RedirectHistory=AkWK5rsBewVTlR3T2Qg|AsmKpuYBMR8tlR3T2Qg; orgName=outlook.com; domainName=; LI=1:XYdQGJ8o9N1cVP0PLAMPKYX04Lo%2bQ173ZE2bDYs0qbM%3d:H4sIAAAAAAAEAGNkYGBgZIAAViib0QDEE0lLzcmsSM4vdcgvLcnJz8/WS87PZQJKCBtY6hsY6hsZGBkpGBhbGZhYGRozg7QZsgBJlpCi0lQAekBLo1YAAAA=; OutlookSession=63765f2d24eb443080fbccb28ec417ac; ShCLSessionID=1641697456425_0.6222671299908159"
cookie = dictcookies(cook1es)
header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:95.0) Gecko/20100101 Firefox/95.0'
}

response = requests.get("https://outlook.live.com/mail/0/", headers=header, cookies=cookie)
et = etree.HTML(response.text)
oi = et.xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/span')
print(oi) # I LOVE EMPTY LISTS
