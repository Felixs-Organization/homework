import requests
import json
import subprocess
import rich
import pandas as pd

# 127.0.0.1:53446
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

rich.print("[green][+] Server responded with 200 OK, we are golden![/]" if response.status_code == 200 else "[red3 blinking][-] Server responded with {}, quitting![/]".format(response.status_code))

if response.status_code != 200:
    exit(1)

rich.print("[grey][+] Dumping resp_json[/]")


resp_jsonp = json.dumps(response.json(), indent=4)
resp_json = response.json()

with open('herolist.json', 'w') as f:
    f.write(resp_jsonp)




# Start getting the columns for the xlsx file

rich.print("[grey][+] Getting the columns for the xlsx file[/]")
hero_names, enames, cnames, titles, pay_types, new_types, hero_types, skin_names = [], [], [], [], [], [], [], []
for hero in resp_json[0]:
    print(hero)
    hero_names.append(hero['hero_name'])
    enames.append(hero['ename'])
    cnames.append(hero['cname'])
    titles.append(hero['title'])
    pay_types.append(hero['pay_type'])
    new_types.append(hero['new_type'])
    hero_types.append(hero['hero_type'])
    skin_names.append(hero['skin_name'])

rich.print("[grey][+] Got the columns for the xlsx file[/]")
rich.print("[grey][+] Setting up the dataframe[/]")
df = pd.DataFrame(
    columns = ["hero_name", "ename", "cname", "title", "pay_type", "new_type", "hero_type", "skin_name"],
    data={
        "hero_name": hero_names,
        "ename": enames,
        "cname": cnames,
        "title": titles,
        "pay_type": pay_types,
        "new_type": new_types,
        "hero_type": hero_types,
        "skin_name": skin_names
    }
)

rich.print("[grey][+] Setting up the writer[/]")
writer = pd.ExcelWriter('herolist.xlsx')
df.to_excel(writer, 'herolist')
rich.print("[grey][+] Writing the xlsx file[/]")
writer.save()
rich.print("[green][+] Done![/]")

exit(0)