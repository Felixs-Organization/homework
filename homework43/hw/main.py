import requests
import pandas as pd


proxies = {
    'http': 'http://127.0.0.1:53446', 
    'https': 'http://127.0.0.1:53446'
}
filename = "results.xlsx"


urls = []
results = []
ids = []
urls_ = {}

for _ in range(4, 8):
    urls.append("https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=18368d9c1707266a2b98935c1e74249d&desktop=true&page_number={}&limit=10&action=down&after_id=17&ad_interval=-10".format(_))



headers= {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:103.0) Gecko/20100101 Firefox/104.0',
    'Cookie': '_xsrf=t4Kp8rz5YNLp1NBL6YegdTxDDfSOPNcz; _zap=823635f3-6300-4891-9e4f-76f84b65528d; d_c0="ABBeeM8q8BSPTrAWUHzNM6DO58_QpH5Js48=|1652494733"; z_c0=2|1:0|10:1657939481|4:z_c0|92:Mi4xSll1aEhRQUFBQUFBRUY1NHp5cndGQmNBQUFCZ0FsVk5HWFNfWXdBQmRhZEJXaHVtVjZJVkVhNjY0bUQ0ZC1vdFV3|1c6c46cd0d0ba3231a236036e1f588359d628ac0f22951047090656e2a408d73; q_c1=48d2dbe3ef0141ca97d19992b1dda647|1657939482000|1657939482000; KLBRSID=4843ceb2c0de43091e0ff7c22eadca8c|1662172170|1662172044; tst=r; SESSIONID=Ktna8hh34umNpUTvSDYSx73qnzVUoqKxrFF3RGuCSSk; NOT_UNREGISTER_WAITING=1; JOID=V1wdAkKb_atdobaqbJ9w-WmY_-Z00YXMNJXfzlajicoa2e__FgNDuDqsu69tTd-_rO5dRD_EMpLsqJe45OPKB9w=; osd=VlgWA06a-aBcrbeuZ558-G2T_up11Y7NOJTbxVeviM4R2OP-EghCtDuosK5hTNu0reJcQDTFPpPoo5a05efBBtA='
}


for url in urls:
    response= requests.get(url, headers=headers, proxies=proxies).json()
    for _ in [1,2,3,4,5]:
        ids.append(response["data"][_]["target"]["id"])


for _ in ids:
    urls_[_] = ("https://www.zhihu.com/api/v4/comment_v5/answers/2533572106/root_comment?order_by=score&limit=20&offset=".format(_))



for _id, url in urls_:
    response = requests.get(url, headers=headers, proxies=proxies).json()
    contents = response["data"][0]["contents"]


