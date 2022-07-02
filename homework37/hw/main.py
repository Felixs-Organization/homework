import requests
import json
import os

url = 'https://haokan.baidu.com/web/video/feed?tab=recommend&act=pcFeed&pd=pc&num=30&shuaxin_id=1655574503671'

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12.00; rv:101.0) Gecko/20100101 Firefox/101.0'
}


proxies = {
    "http": "http://127.0.0.1:53446",
    "https": "http://127.0.0.1:53446"
}

print("Sending Request...")
response = requests.get(url, headers=headers, proxies=proxies)

print("200 OK" if response.status_code == 200 else "NOT OK")

if response.status_code != 200:
    exit(1)


resp_json = response.json()

print("Writing resp.json...")

with open('resp.json', 'w') as f:
    f.write(json.dumps(resp_json, sort_keys=True, indent=4))


if not os.path.exists('videos'):
    os.mkdir('videos')


print("Writing URLS to videos/urls.txt...")



urls = []
with open('videos/urls.txt', 'w') as f:
    i = 0
    for dicty in resp_json["data"]["response"]["videos"]:
        url = dicty["url"]
        f.write(url + '\n')
        urls.append(url)
        i += 1


print("Downloading videos...")
i = 1
for url in urls:
    file = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12.00; rv:101.0) Gecko/20100101 Firefox/101.0'})
    filename = 'videos/%d.mp4' % i
    with open(filename  , 'wb') as f:
        f.write(file.content)
    print("Downloaded video %s" % filename)
    i += 1


print("Finished!")

exit(0)