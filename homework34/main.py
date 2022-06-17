import requests
from lxml import etree
import os
import re
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:97.0) Gecko/20100101 Firefox/97.0"
}
url = "https://top.baidu.com/board?tab=novel"
response = requests.get(url, headers=headers)
xpath_text = '//*[@id="sanRoot"]/main/div[2]/div/div[2]/div/div[2]/a/div/text()'
xpath_img = '//*[@id="sanRoot"]/main/div[2]/div/div[2]/div/a/img/@src'
print("Sucess" if response.status_code == 200 else "Fail")
html = etree.HTML(response.text)
names = html.xpath(xpath_text)
images = html.xpath(xpath_img)
print('Length of names:', len(names))
print('Names: ', names)
print('Length of images:', len(images))
print('Images: ', images)
print("Downloaing images... This might take a while")
i = 0
if not os.path.exists('images'):
    os.mkdir('images')
for image in images:
    i += 1
    print("Downloading image %d" % i)
    response = requests.get(image, headers=headers)
    with open('images/%d.jpg' % i, 'wb') as f:
        f.write(response.content)
print("Finished!")
