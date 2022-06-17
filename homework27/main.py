import requests

paramaters = {
    'wg': 'sony'
}

'''
def dictcookies(cookiestext):
    cookies = {}
    cookiespure = cookiestext.replace(' ','')
    cookieslist = cookiespure.split(';')
    for i in cookieslist:
        key.value = i.split('=',1)
        cookies[key] = value
    return cookies
'''
ddg = "https://duckduckgo.com"
ddg_lite = "https://lite.duckduckgo.com/lite"
baidu = "https://www.baidu.com"
header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:96.0) Gecko/20100101 Firefox/96.0'
}
response = requests.get(ddg, params=paramaters, headers=header) # cookies=dictcookies("aq=-1; l=us-en; ak=-1; ax=-1; ay=b; 5=2; ar=1"

file = open('ddg.html', 'w', encoding='utf-8')
file.write(response.text)
file.close()