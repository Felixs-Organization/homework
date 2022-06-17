import requests



url = "https://pocket-image-cache.com/direct?resize=w2000&amp;url=https%3A%2F%2Fhbr.org%2Fresources%2Fimages%2Farticle_assets%2F2015%2F10%2Foct15-14-511824675.jpg"


file = open('image.jpg','wb')


response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu 21.10; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/69.420'})

file.write(response.content)
file.close()

