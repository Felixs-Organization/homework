import requests
import json


proxies = {
    'http': 'http://127.0.0.1:53446',
    'https': 'http://127.0.0.1:53446'
}

# Title, Comments, Like, Forwards
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12; rv:102.0) Gecko/20100101 Firefox/69.0',
    "Accept": 'text/html, application/json',
    "Cookie": '_xsrf=t4Kp8rz5YNLp1NBL6YegdTxDDfSOPNcz; _zap=823635f3-6300-4891-9e4f-76f84b65528d; d_c0="ABBeeM8q8BSPTrAWUHzNM6DO58_QpH5Js48=|1652494733"; captcha_session_v2=2|1:0|10:1657939457|18:captcha_session_v2|88:SUxBU1NLWFpIaGZYNUpJU05Vc0hFL1hFdGhsU0ZxK1VWL2duSFZZaVZBbHNTNHR1TllxQ0tKWXltOTNOTnBXMw==|ceb39c2eb6a75e7ba3329dfe69a9422c5979d8b0962929b86a8b6e220a10bab6; __snaker__id=manWJdzzW2FuxqqS; gdxidpyhxdE=R%5C8EAGO6mUshRalk3v%5C9RLIrmHgUYNEwqzDSOaZiRH4ByCfoQ4SQBA6IuaVOjPhqukQ%5CUPN1zwghAQ9bN%5CI85hVc3H%2FMZaqogT%2B2pDlwe2Ck0nJWXsmuLi%2Fibd3AaQAMP6%2FZMyUJeox0yobriU15DMO52OBb%2BxmB56vTBbpsj%2FnWUcWD%3A1657940368258; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=z3eHFpmHm4SHwn6BfYrIuju4qfy%2F1GD%2BneqNPukhQTo%2BpHTunndwSf1qLqfrSOk4sLAr%2BaoERrPjWPakQLcYNn7ILNhxhhXVQ9FerTPkR3N6E5Maml7FCXtPyYUOePlzVWs%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea6bc25f4eda799cb41a1eb8fa6c54e878e9ab0d85d838ba993c6548ab0b694b52af0fea7c3b92abaedaba9c57caf98a3d5d244b5b2faa3e553b297bb8bf840b3bab7d0b44d88f5a286f44694aba589d460adf5c0a9d77faeb2ac98d26ef3af8492e57a9191a5d5f24883aee582ee4f92aea08bd65ca3b59fade2538eb2f9aacf46aca8a889db5e93e78a86f16094b59ed4cd3e87eb8382f068f59a8db9f75cbb879bb0e85cb0a69ab8f237e2a3; YD00517437729195%3AWM_TID=T3VzZ2lh%2F5pEUEFBABKATQRhuXXJo3tq; z_c0=2|1:0|10:1657939481|4:z_c0|92:Mi4xSll1aEhRQUFBQUFBRUY1NHp5cndGQmNBQUFCZ0FsVk5HWFNfWXdBQmRhZEJXaHVtVjZJVkVhNjY0bUQ0ZC1vdFV3|1c6c46cd0d0ba3231a236036e1f588359d628ac0f22951047090656e2a408d73; q_c1=48d2dbe3ef0141ca97d19992b1dda647|1657939482000|1657939482000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1657939569,1658093515; KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1658093600|1658093510; SESSIONID=uBhv6Jwqxj5I34fN1OT1ATNMIMGybT4FWJmtXq3jcbc; NOT_UNREGISTER_WAITING=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1658093551; JOID=UVAcAEOMJccf82-7DoylkiXKIvoR8malYs4uzXX_RPNcy1DWQUxREn3zZbAPr6Mx0qFR_PcMJjUrwZGtnOCwCWM=; osd=VFkRBU6JLMoa_mqyA4molyzHJ_cU-2ugb8snwHDyQfpRzl3TSEFUH3j6aLUCqqo816xU9foJKzAizJSgmem9DG4=; tst=r'
}
url1 = "https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=b02a267b0e3323b876e99999feed7a19&desktop=true&page_number=5&limit=400&action=down&after_id=23&ad_interval=-10"
urls = []


for num in range(3, 135):
    urls.append(url1.replace("page_number=5", "page_number=" + str(num)))

i = 0
for url in urls:
    i += 1
    response = requests.get(url, proxies=proxies, headers=headers)
    resp_json = response.json()
    for post in resp_json["data"]:
        if i == 1: # if i is 1, then...
            # open the file "data.txt" and write the number of comments, voteups, thanks, author name and the title/headline
            with open('data.txt', 'w') as f:
                f.write(f'{i}: \t Comments: {post["target"]["comment_count"]} \t Voteup count: {post["target"]["voteup_count"]} \t Thanks count: {post["target"]["thanks_count"]} \t Author Name: {post["target"]["author"]["name"]} \t Title: {post["target"]["author"]["headline"]} \n')
        else:
            with open('data.txt', 'a') as f:
                f.write(f'{i}: \t Comments: {post["target"]["comment_count"]} \t Voteup count: {post["target"]["voteup_count"]} \t Thanks count: {post["target"]["thanks_count"]} \t Author Name: {post["target"]["author"]["name"]} \t Title: {post["target"]["author"]["headline"]} \n')
with open("resp.json", 'w', encoding='utf-8') as f:
    json.dump(resp_json, f, ensure_ascii=False, indent=4)

'''
Data:
    - comment: 
'''
