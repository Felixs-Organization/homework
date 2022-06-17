from bs4 import BeautifulSoup


with open('html/index.html', 'r', encoding="UTF-8") as f:
    soup = BeautifulSoup(f, 'lxml')
    print("soup.a: ", soup.a)
    print("soup.find: ", soup.find('a'))
    print("soup.find_all: ", soup.find_all('a'))
    print("soup.find_all(id='geturllink'): ", soup.find_all(id='geturllink'))
    print("soup.find_all(class_='geturllink'): ", soup.find_all(class_='geturllink'))