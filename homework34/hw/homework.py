import requests
from lxml import etree
import time

"""



 思路
 输入什么小说的名字 就可以爬取什么小说
 有个post请求
 第一步 爬取一个小说的所有章节的超链接
 第二步做一个函数 函数的功能是爬取一章的内容 并写入到文件
 第三步通过超链接的列表 调用第二步的函数 把每一章的内容写入到文件内

"""


def f(u):
    global p
    url = "https://www.xbiquge.la/" + p
    resp = requests.get(url)
    resp.encoding = "utf-8"
    sus = etree.HTML(resp.text)
    xpathing = sus.xpath('//*[@id="content"]/text()')
    con = open(p + ".txt", "a", encoding="utf-8")
    for i in xpathing:
        con.write(i)
    con.close()


def get(url):
    url = url
    a = requests.get(url)
    a.encoding = "utf-8"
    s = etree.HTML(a.text)
    b = s.xpath('//*[@id="list"]/dl/dd/a/@href')
    for i in b[:10]:
        time.sleep(0.5)
        f(i)


p = input("Please enter the name of the book\n")
url = "https://www.xbiquge.la/modules/article/waps.php"
data = {"searchkey": p}
response = requests.post(url, data=data)
response.encoding = "utf-8"
s = etree.HTML(response.text)
url = s.xpath('//td[@class="even"]/a/@href')
get(url[0])
