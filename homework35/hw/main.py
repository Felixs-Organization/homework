import requests
import json

'''
作业
https://weibo.com/newlogin?tabtype=weibo&gid=102803&openLoginLayer=0&url=https%3A%2F%2Fweibo.com%2F
发表人的名字
'''

url  = 'https://weibo.com/newlogin?tabtype=weibo&gid=102803&openLoginLayer=0&url=https%3A%2F%2Fweibo.com%2F'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'cookie':'_zap=78c2bda7-9bd3-47f0-9a71-40dcd40bff8a; _xsrf=CDxZMcq2UOOcwkSv2trzEN6um4ZCqU7c; d_c0="AXBR164lIBSPTu-NGVAqW0FcQKWYAQfUvfk=|1638534745"; __snaker__id=rkbGfvcq7IVzyaJd; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=w8lO%2Fz6x3MlBFAUEBUNrsoUFYNFCeG4k; gdxidpyhxdE=YJJc9QQsXtjYK0kLK%5C9Vq6aIczRcmtbv%5CicOkrDWaMOevstDrKCAKpmZNwU2SbUxQ7yWxNSfHBt3mJ7G2PdZZAETw17xvYD9zlykGOIoyLWoXlkY6JqDj6%5CwINfey2OQ4PNx725iNbpH%2FMegULm%2F%5CgSHLC2%5CBCIPr715eTOAshSpUnBx%3A1640390233813; YD00517437729195%3AWM_NI=RgU%2BVR9mrmzsNslnIAcQnnsnozxjnpSkkgDiqr%2FgSd7o%2FnRpJfnzlo%2B4G46BYDpGkXCd9f%2Fh%2F%2FiV0at%2FvommHOIONOg0wZKjskrLP%2B0t7AqyCrbAepTD4NAoRa1ombf1OTE%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeafed3cadadabbaec3caeeb8aa7d45f838b8aaff180b7b7bd90f666aa86bea8ee2af0fea7c3b92a92b99bccd55afbb3be8ef9798eada48fcc4ba18fa28ff266ada6b88bed7c91b5a588c763b3aee188d270f5b1e18fd17c8abaa29bef65e9ec89d5b54a9b9cc0a8ea5481bcf787ae64edf1a7b7b36bb8f1ba90f0678c9187b0cd45a5f0b9bbca62b1b5beadd321f4acf9a2f47381aeaea2e87c989cfcafc46592bfff90f06aa6ef81b5c837e2a3; z_c0=Mi4xSll1aEhRQUFBQUFCY0ZIWHJpVWdGQmNBQUFCaEFsVk42YWl6WWdCTHJJSGNiWl9Xb29YRXgzdWM5QUQ2WWthMlpn|1640389353|a47993d2c47ddd00efd27179da119dc04efd189f; q_c1=14ca4a533ace4874b236d32bb5817dbd|1647745950000|1647745950000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1651666436,1651924380,1651972075; NOT_UNREGISTER_WAITING=1; SESSIONID=PryahcaXxBbtPgSdKGzCXiYLMuW5nauJzw1adHlhfif; JOID=U10dAE0u321vfKLiGiwsue7dhcEHeqAfCxPFjklRmQIQKcK1c8jOFA9_q-QUqzKpu6wnLXXxlHU_eKDbBFdvxXc=; osd=UV4SBkos3GJpe6DhFSoru-3Sg8YFea8ZDBHGgU9WmwEfL8W3cMfIEw18pOITqTGmvaslLnr3k3c8d6bcBlRgw3A=; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1651972503; BAIDU_SSP_lcr=https://www.baidu.com/link?url=mQh0BhN0_sSE0-0EJCSxJo3wLZdiFnRoU7qqf48o9sG&wd=&eqid=d4c1b38a00001c4100000002627717e2; KLBRSID=cdfcc1d45d024a211bb7144f66bda2cf|1651972575|1651972070'

}

con = requests.get(url,headers=headers).json()



print(con['data'][0]['target']['excerpt'])



print(type(con.text))



ccc = json.loads(con.text)

print(type(ccc))

print(ccc)







