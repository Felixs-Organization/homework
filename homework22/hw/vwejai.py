#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree



path = '//html/body/div[1]/div[4]/div[1]'

url = 'https://i.qq.com/?s_url=http%3A%2F%2F1284631404.qzone.qq.com%2F'
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:95.0) Gecko/20100101 Firefox/95.0', 'Cookie': 'next-i18next=en; OptanonConsent=isIABGlobal=false&datestamp=Sat+Dec+18+2021+18%3A33%3A47+GMT-0800+(Pacific+Standard+Time)&version=6.14.0&hosts=&consentId=c988a4f6-f06a-4395-9e9d-f90b83a6485a&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=%3B; sess_start_time=1613940381; _sp_id.ae42=a529c9d4-eb43-4c49-b7a2-994efaf47639.1614221164.10.1639881247.1639787239.0464fdfb-9a6e-44f9-a069-74164db69f96; _omappvp=ZlKC4TR9Jvihc594Ub0yNESqNStk9ZVlbLuyCyqWMmV8R1i17HS9wmDTFSurn511iOlIXAxr5Z4Z4sgqHGCLDsXWWJf9ulXa; sp=a5cdfa20-6f97-401f-aa59-4f30e6697091; _ga=GA1.2.273113553.1614221165; sess_guid=8e0p6T29Ac61ad109cgHj21Ga6dOA258438A8ah5e2pKMRi6d545cf8aG76DQemn; OptanonAlertBoxClosed=2021-12-04T03:18:47.700Z; PHPSESSID=a72184dd9c9caca7239fbe8c14cdd0ba; AUTH_BEARER_default=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJpYXQiOjE2Mzk4ODEyMjYsImp0aSI6InBmT0dJTDhaXC8xelhvRUdsMWtLb3VzaUdySXZ5YUtMYXdvVGRPdkU3QU1JPSIsImlzcyI6ImdldHBvY2tldC5jb20iLCJuYmYiOjE2Mzk4ODEyMjYsImV4cCI6MTYzOTg4NDgyNiwiZGF0YSI6Il9zZjJfYXR0cmlidXRlc3xhOjA6e31fc3ltZm9ueV9mbGFzaGVzfGE6MDp7fV9zZjJfbWV0YXxhOjM6e3M6MTpcInVcIjtpOjE2Mzk4ODEyMjY7czoxOlwiY1wiO2k6MTYzOTg4MTIyNjtzOjE6XCJsXCI7czoxOlwiMFwiO30ifQ.HPTc2bnhNtrNDtuhObKxH9pxk5KbE-kC3PTr3rTEpwBcYxpcNB0Xc5fGlr7x3T8i-VNs33A0PqksPDqGiJX6jvvpjsULPEZD3DJFBprWh6PHiRlIlv839_Ks2JyaG1VXRxuRR1_VDMz2bm5pmwtqpWtYVku9QNEMyxP4Wu7OkBAByGoT0vfKAGxHdhrjPYjoPNgNyKZb1ocZiRy0r3ST0dH6n6u1vF45iBjZNPfpjs1wfn-0ri5ltMaNe2NfgPgfYAR0IgdfYP0cV1LjmAfNcKewKy6Jwx-Hcrp2plIqDfZe16vcPiKk6at5aU5DgYIA1GdFThHw26wxeZkKZGejeQ; _sp_ses.ae42=*'}


r = requests.get(url, headers=header)
r.encoding = 'utf-8'

page = etree.HTML(r.text)
hh = page.xpath(path)
a = input('raw list or 0.text? 1/2\n')

if a == '1':
    print(hh)
elif a == '2':
    print(hh[0].text)
