import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu 21.04; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/69.0'} # This tricks the server into thinking that we're using Ubuntu 21.04 and Firefox 69.0.




def find_elem(elem, url, headers):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
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



