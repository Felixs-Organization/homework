import requests





cookie_text = "flwssn=7b343b8a-3cb8-43d0-b2a0-545a359cc165; clSharedContext=1e48b46f-6f81-405e-a742-6127d9563847; nfvdid=BQFmAAEBEOnT70gTCJ0exKUdR-8H2AdAO52MQf71npRV1k_2knq95sYVLZEryalf-gqiyZlpdDqoRUgyjzsr1A0g1YTuAtnYiGeujWr5-f3DSDB-VmP5mQ%3D%3D; SecureNetflixId=v%3D2%26mac%3DAQEAEQABABRl8SjYFqr7d_w-Ph7w40gN1Yhv0Fzhguc.%26dt%3D1644718432763; NetflixId=v%3D2%26ct%3DBQAOAAEBEL9cTH0lOX7tkSpnl1R7n1uBAMl4joilYTfuNAKJHWggR_YaLaPPNoU0cSRo4pwpB0Hd7P9d6HjsYYGR4SZTVn0DBDvUZxG-nBewTw4-Md2ymGBuEN3cIXN0zQmQ588S2Bq6FzLW4v8MXlKmuQXI9zKF…LWAiZyFOux1nM6EP3rDXUKgu8Q.; memclid=43ef78c3-42f8-4832-8bcd-126b78fe9b79; cL=1644719204578%7C164471843331457311%7C164471843374914812%7C%7C18%7Cundefined; OptanonConsent=isIABGlobal=false&datestamp=Sat+Feb+12+2022+18%3A26%3A45+GMT-0800+(Pacific+Standard+Time)&version=6.6.0&consentId=0fbd5984-aab1-41ff-bdf0-60d9d496553b&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1&hosts=H12%3A1%2CH13%3A1&AwaitingReconsent=false&geolocation=US%3BCA; OptanonAlertBoxClosed=2022-02-13T02:26:45.639Z"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12; rv:97.0) Gecko/20100101 Firefox/97.0"
url = "https://www.netflix.com/personalization/cl2"
header = {
    "User-Agent": user_agent,

}

response = requests.post(url=url, headers=header)
print(response.status_code)