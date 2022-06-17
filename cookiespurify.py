def dictcookies(cookiestext):
    cookies = {}
    cookiespure = cookiestext.replace(' ','')
    cookieslist = cookiespure.split(';')
    for i in cookieslist:
        key.value = i.split('=',1)
        cookies[key] = value
    return cookies
