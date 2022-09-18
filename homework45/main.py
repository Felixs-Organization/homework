import requests
import json
import pygal
from rich import print as rprint



headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:104.0) Gecko/20100101 Firefox/104.0',
        'Cookie': 'pgv_pvid=9642922160; isHostDate=19252; PTTuserFirstTime=1656028800000; isOsSysDate=19252; PTTosSysFirstTime=1656028800000; isOsDate=19252; PTTosFirstTime=1656028800000; ts_uid=3855853188; weekloop=0-0-0-38; eas_sid=v1o6y5E6W1w2g6Y0V869I6w9b9; pgv_info=ssid=s2005791018; ts_last=pvp.qq.com/web201605/herolist.shtml; pvpqqcomrouteLine=herolist_herodetail_herolist; PTTDate=1663469658841; ieg_ingame_userid='
}


proxies = { 'http': 'http://127.0.0.1:53446', 'https': 'http://127.0.0.1:53446' }

rprint("[light_grey]\[*] Sending request[blink].[/][blink].[/][blink].[/] [/]")
response = requests.get('https://pvp.qq.com/web201605/js/herolist.json', headers=headers, proxies=proxies)

rprint("[green]\[+] 200 OK [/]" if response.status_code == 200 else "[red][bold]\[-] Whoops, we didn't get a 200 OK. Something's fishy...[/][/]")
