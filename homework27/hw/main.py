import requests
from lxml import etree


url='https://translate.google.com/'
wd = input('input your fn?: ') #输入想要搜索的内容
param = {
    'wd': wd,
    }
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:96.0) Gecko/20100101 Firefox/96.0'
    }

response = requests.get(url=url, headers=headers) # temp params: 
text = response.text
filename = '%s_search_results.html' % wd

with open(filename, 'w', encoding='utf-8') as file:
    file.write(text)


print('baidu search results saved to %s' % filename)