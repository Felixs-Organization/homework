import requests
from lxml import etree

url = "https://locations.kfc.com/search?qp=Orinda, California 94563, United States&r=20&q=37.88,-122.18"


xpaths = [
    "/html/body/main/div/div[2]/div[2]/div[4]/div/div[2]/ol/li[1]/article/div[2]/address",
    "/html/body/main/div/div[2]/div[2]/div[4]/div/div[2]/ol/li[2]/article/div[2]/address",
    "/html/body/main/div/div[2]/div[2]/div[4]/div/div[2]/ol/li[3]/article/div[2]/address",
    "/html/body/main/div/div[2]/div[2]/div[4]/div/div[2]/ol/li[4]/article/div[2]/address"
]
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:97.0) Gecko/20100101 Firefox/97.0"
}
response = requests.get(url, headers=headers)


html = etree.HTML(response.text)
for xpath in xpaths:
    print(html.xpath(xpath))
