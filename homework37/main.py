import requests
import os
import json


url = "https://haokan.baidu.com/web/video/feed?tab=recommend&act=pcFeed&pd=pc&num=21&shuaxin_id=1655522082555"

headers = {
    "Cookie": 'BAIDUID=2BA944C578A343FD1DEDDE1FF65F94EA:FG=1; BIDUPSID=2BA944C578A343FDBAC8E4DBF0BDAAD8; PSTM=1629773901; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1654915941,1655522083; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1655522083; ab_sr=1.0.1_ZDFkMDEwOThiOGM0ZTU1ZmE0NmRkMjg5YmFkOWYxODI2OGQxNWQ1ZDExYzNlNjhmYWQzNTAzMzM3N2FjYjBjNTVlOTQ5NTBkMjliZWE1ODJkYTczMjQxZmRkNjFkMDRiYTUzM2VlNjRhMWJjNjBjZWIwYzE0MThjMTRlNTA5MDY4YTU4NTE3ZmJhNTNmYzliOGI2ZGUwNzU1YjAyOWMzNg==; reptileData=%7B%22data%22%3A%2216c3b3f0d436510b3049e1a66a5667d7c870fcb1bfb9818fbfd7414bb2867d7da8d7e36ce4e92c922f7caf33de79e157a685940858f1b60b710451c6747da961ad2c9787910df58fcf812b525326609e5f9077068e6d92fb257dc5e015118b61%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%22b8aeb399%22%7D; RT="z=1&dm=baidu.com&si=c5im5juapj9&ss=l4jb3kpr&sl=1&tt=n8g&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=o8l',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.00; rv:101.0) Gecko/20100101 Firefox/101.0"
}



response = requests.get(url, headers=headers)

print("OK" if response.status_code == 200 else "NOT OK")

resp_json = response.json()

print("Writing resp_json to resp.json...")
with open("resp.json", 'w') as f:
    f.write(json.dumps(resp_json))
print("Done!")


print("Making dir videos")
os.mkdir("./videos")

print("Now for the fun bit, writing the videos!")

