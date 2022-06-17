#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests



url = "https://malwarewatch.org"
ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 OPR/73.0.3856.284"



def find_elem(response, elem):
    text = response.text
    elem1 = text.find(elem) # elem1 = the first <> pair, elem2 = the second <> but has a / (like </>)
    elem2 = ""
    for i in range(len(elem)):
        if i == 1:
            elem2 += '/'
            elem2 += elem[i]
        else:
            elem2 += elem[i]
    elem3 = text.find(elem2)
    return text[elem1+7:elem3]



def find_text(url):
    headers = {'User-Agent': ua}
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    return find_elem(r, '<h1>')


print(find_text("https://malwarewatch.org"))