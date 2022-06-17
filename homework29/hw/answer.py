import requests
import rich
url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:97.0) Gecko/20100101 Firefox/97.0"
}

place = input("Search for KFC's in which Chinese city? (please be chinese): ")

print("Chinese KFC search starting...")
print("Searching for KFC's in {}...".format(place))
print("Please stand by.")
data = {
    "cname": "",
    "pid": "",
    "keyword": place,
    "pageIndex": "1",
    "pageSize": "10",
}
response = requests.post(url=url, headers=header, data=data)
print("Sucessfully got response from KFC's website.")
if response.text != None and response.status_code == 200:
    filename = "kfc_" + place + "_search_results.txt"
    print("Writing to file {0}...".format(filename))
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)
    print("Successfully wrote to file:", filename)
    print("KFC search sucessful.")
else:
    print("KFC search failed.")
    print("Status code: %s" % response.status_code)
    print("Response text: %s" % response.text)