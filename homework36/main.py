import requests

url = "https://us.tiktok.com/api/post/item_list/?aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0 (Macintosh)&channel=tiktok_web&cookie_enabled=true&device_id=7107810650311788078&device_platform=web_pc&focus_state=false&from_page=user&history_len=8&is_fullscreen=false&is_page_visible=true&os=mac&priority_region=&referer=&region=US&root_referer=https://www.tiktok.com/&screen_height=1440&screen_width=2560&tz_name=America/Los_Angeles&webcast_language=en&msToken=7gt6Bg8EZOOm3IvF0D1z4qY0Bf8NhWN0EAhSHxTCN8uurGjgPz9aufO1H2sJv02HJSbKv9EM8vr6PrWkevrMtxZyeA3D8As-f5DLJs-Ko_CCzCR7PAEQNqgZNhW0vQ==&X-Bogus=DFSzsIjYn60ANHtpSvpk6iituT1B&_signature=_02B4Z6wo000012JITDAAAIDAdc0kltxSGEtiSUCAALpB09"

headers = {
    "Cookie": "ttwid=1%7CSrncsAj-LMMw2QqYBT6SSRWXthtauHTkek_Dhoo9SHY%7C1654916335%7C36b7ee653293f1d886bf0720a5e1543f6158e8b3ffc279f76e8f219d30411ccb; tt_csrf_token=uEJBSbYE-1S3d_1IPfzDcKbC5FY6Okj30WMo; msToken=AZ4ix5H2eYReyuJfrM9g1yqbP6oAd2oELL5djO-LZNoLMHE86toyk4Khik_b93ixQd_cwIHFdsw8j1E28D1sBqLSFjC8mZATIG3fgnDa5yXPIJovVq2iN_a7X5LLtgTHDf4nhMWAJPRF; _abck=F742B6D0F5C634F7388778511F62F1B7~-1~YAAQGVXRF9LI0y2BAQAAqUSwUAhJtCh4glLTKnv+bfWWY6AMwBcfiRkOBAzRXM0YfDIfcWWP9ik2N2kHqDgi/xZr1TxG39FbBvkWl//iHw/NZgIUvdBsJ9YNxzPeIFij8OMeX…sessionid=867d51b1ee41ea3207060fe44a8c5983; sessionid_ss=867d51b1ee41ea3207060fe44a8c5983; sid_ucp_v1=1.0.0-KGExMTMyZGU4MTNiNzc5YzE1ZjczNWMxNDkyYTc3NWQ4ZGFhZjZkMjcKHwiGiN-I8OjD514Q0ImQlQYYswsgDDC2n7z2BTgIQBIQBBoHdXNlYXN0NSIgODY3ZDUxYjFlZTQxZWEzMjA3MDYwZmU0NGE4YzU5ODM; ssid_ucp_v1=1.0.0-KGExMTMyZGU4MTNiNzc5YzE1ZjczNWMxNDkyYTc3NWQ4ZGFhZjZkMjcKHwiGiN-I8OjD514Q0ImQlQYYswsgDDC2n7z2BTgIQBIQBBoHdXNlYXN0NSIgODY3ZDUxYjFlZTQxZWEzMjA3MDYwZmU0NGE4YzU5ODM; store-idc=useast5; store-country-code=us; tt-target-idc=useast5",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:101.0) Gecko/20100101 Firefox/101.0"
}

response = requests.get(url)
response.encoding = "utf-8"
resp_json = response.json()

print("OK" if response.status_code == 200 else "Error")

print("Writing resp_json to file")

with open("resp_json.json", "w") as f:
    f.write(str(resp_json))

print("Done!")

