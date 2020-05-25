#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import re
import requests
from multiprocessing import Pool, Manager

from Config.config_hawkeye import Port_HTTP, Port_HTTPS
from Config.config_requests import headers
from Core.decorators import Save_info
from Tools.cidr_ip import Cidr_ips

requests.packages.urllib3.disable_warnings()




def Get_urls(cidr):
    if re.match(r"^(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\/([1-9]|[1-2]\d|3[0-2])$",cidr):
        try:
            urls=[]
            ips = Cidr_ips(cidr)
            for ip in ips:
                for i in Port_HTTP:
                    urls.append('http://'+str(ip)+':'+str(i))
                for j in Port_HTTPS:
                    urls.append('https://'+str(ip)+':'+str(j))
            return urls
        except:
            pass
    else:
        pass

def Get_tile(url,res,q):
    try:
        r=requests.get(url,headers=headers,timeout=3,verify=False)
        rule = re.compile(r'<title>(.*?)</title>')
        title = rule.findall(r.text)
        if title:
            print(url+'  '+str(r.status_code)+'  '+title)
            res.append(url+'  '+str(r.status_code)+'  '+title)
        else:
            print(url + '  ' + str(r.status_code) + '  ' + r.text.replace('\n','')[0:30])
            res.append(url + '  ' + str(r.status_code) + '  ' + r.text.replace('\n','')[0:30])
    except:
        pass
    q.put(url)

@Save_info
def Hawkeye(cidr):
    res = Manager().list([])
    p = Pool(30)
    q = Manager().Queue()
    urls=Get_urls(cidr)
    print('侦测开始~加载任务量：{}条'.format(len(urls)))
    if urls:
        for i in urls:
            p.apply_async(Get_tile, args=(i,res,q))
        p.close()
        p.join()
        return res
    else:
        print("CIDR格式输入有误，锤你昂w(ﾟДﾟ)w")


def run(cidr):
    Hawkeye(cidr)

if __name__ == '__main__':
    print(Get_tile('https://github.com/rabbitmask/AssetsHunter'))
