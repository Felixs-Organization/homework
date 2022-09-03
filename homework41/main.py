import requests
import json
import pandas


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Cookie': '_xsrf=t4Kp8rz5YNLp1NBL6YegdTxDDfSOPNcz; _zap=823635f3-6300-4891-9e4f-76f84b65528d; d_c0="ABBeeM8q8BSPTrAWUHzNM6DO58_QpH5Js48=|1652494733"; captcha_session_v2=2|1:0|10:1657939457|18:captcha_session_v2|88:SUxBU1NLWFpIaGZYNUpJU05Vc0hFL1hFdGhsU0ZxK1VWL2duSFZZaVZBbHNTNHR1TllxQ0tKWXltOTNOTnBXMw==|ceb39c2eb6a75e7ba3329dfe69a9422c5979d8b0962929b86a8b6e220a10bab6; z_c0=2|1:0|10:1657939481|4:z_c0|92:Mi4xSll1aEhRQUFBQUFBRUY1NHp5cndGQmNBQUFCZ0FsVk5HWFNfWXdBQmRhZEJXaHVtVjZJVkVhNjY0bUQ0ZC1vdFV3|1c6c46cd0d0ba3231a236036e1f588359d628ac0f22951047090656e2a408d73; q_c1=48d2dbe3ef0141ca97d19992b1dda647|1657939482000|1657939482000; KLBRSID=ed2ad9934af8a1f80db52dcb08d13344|1659755540|1659755056; SESSIONID=mqMcqM0Z1a9Pg5IJW2acFsWEtI7jlhFhVMWpKBmXqyN; NOT_UNREGISTER_WAITING=1; JOID=VVsSC0NBzTccqVKXPk5GaCaeEN0rKLh1f9cbo2t_qApDzmjacHsc1XGiUpwxuAuQU2V6OsTI8Ix0hrRljVsI7eQ=; osd=U1ASAEpHxjcXoFScPkVPbi2eG9QtI7h-dtEQo2B2rgFDxWHce3sX3HepUpc4vgCQWGx8McTD-Yp_hr9si1AI5u0=; tst=r'
}



url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=f4cbe08fbed6982bffacace6d3b1b2af&desktop=true&page_number=3&limit=6&action=down&after_id=11&ad_interval=-10'


print(f"[*] Sending request to {url}")

#import pdb;pdb. set_trace();
response = requests.get(url, headers=headers)

print("[+] Sucessful GET request" if response.status_code == 200 else "[-] Unsuccessful GET request")
resp_json = response.json()
print("[*] Writing resp.json")


with open('resp.json', 'w', encoding='UTF-8') as f:
    json.dump(resp_json, f, ensure_ascii=False, indent=4)


print("[+] Sucessfully wrote resp.json")

print("[*] Writing resp.xlsx")
df = pandas.DataFrame(resp_json["data"])
df.to_excel('resp.xlsx', index=False)

print("[+] Sucessfully wrote resp.xlsx")

exit(0)
