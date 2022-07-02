import requests
import json
import os
import rich

proxies = {
    "http": "http://127.0.0.1:53446",
    "https": "http://127.0.0.1:53446"
}

headers = {
    "User-Agent": "coding/3.3",
    "Cookie": "pgv_pvid=9642922160; pgv_info=ssid=s8435770066; pvpqqcomrouteLine=herolist; eas_sid=v1o6y5E6W1w2g6Y0V869I6w9b9"
}

url = 'https://pvp.qq.com/web201605/js/herolist.json'

rich.print("[grey][+] Requesting /web204605/js/herolist.json from pvp.qq.com[/]")
response = requests.get(url, headers=headers, proxies=proxies)

rich.print("[green][+] Server responded with 200 OK, we are golden![/]" if response.status_code == 200 else "[red][-] Server responded with {}[/]".format(response.status_code))
rich.print("[grey][+] Printing resp_json[/]")


resp_jsonp = json.dumps(response.json(), indent=4)
resp_json = response.json()

with open('herolist.json', 'w') as f:
    f.write(resp_json)


rich.print("[grey][+] Enumerating ENAMEs[/]")

