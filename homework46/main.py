import requests
from lxml import etree
from rich import print as rprint
import json
import pygal


radar = pygal.Radar()
radar.title = 'Hero statistics'
radar.x_labels = ['生存能力', '攻击伤害', '技能效果', '上手难度 ']

xpath = '//div[1]/ul/li/span/i/@style'
enames = json.loads(open('enames.json', 'r', encoding='utf-8').read())

headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:103.0) Gecko/20100101 Firefox/104.0', 'Cookie': 'pgv_pvid=9642922160; PTTuserFirstTime=1656028800000; PTTosSysFirstTime=1656028800000; PTTosFirstTime=1656028800000; ts_uid=3855853188; eas_sid=v1o6y5E6W1w2g6Y0V869I6w9b9; isHostDate=19259; isOsSysDate=19259; isOsDate=19259; pgv_info=ssid=s2796907773; ts_last=pvp.qq.com/web201605/herodetail/542.shtml; pvpqqcomrouteLine=herodetail_herolist_herodetail_herodetail; weekloop=0-0-0-39; PTTDate=1664075127548; ieg_ingame_userid=QLPPe8fM1Wv0BqaGRUh4sjXTjbx6PyJf' }

proxies = { 'http': 'http://127.0.0.1:53446', 'https': 'http://127.0.0.1:53446' }



with open('results.txt', 'w', encoding='utf-8') as _:
    for ename in enames:
        rprint(f"[light_grey]\[*] Sending request to ename [bold_dark_red]{ename}[/][blink].[/][blink].[/][blink].[/] [/]")
        response = requests.get(f"https://pvp.qq.com/web201605/herodetail/{ename}.shtml", headers=headers, proxies=proxies)

        text = response.text

        Object = etree.HTML(text)

        responce = Object.xpath(xpath)
        ls = list()
        for item in responce: _.write(f'{item.strip(":")[6:].strip("%")} '); ls.append(item.strip(":")[6:].strip("%"))
        _.write('\n')
        radar.add(str(ename), ls)
        del ls

_.close()

radar.render_to_file('radar.svg')
radar.render_to_png('radar.png')