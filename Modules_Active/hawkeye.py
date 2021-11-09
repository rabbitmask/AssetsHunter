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


def urlcheck(url):
    if 'http' in url:
        return url
    else:
        return ('http://'+str(url))

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
        r=requests.get(url,headers=headers,timeout=10,verify=False)
        rule = re.compile(r'<title.*?>(.*?)</title>')
        title = rule.findall(r.content.decode('utf-8'))
        if title:
            print(url+'  '+str(r.status_code)+'  '+title[0].decode('utf-8'))
            res.append(url+'  '+str(r.status_code)+'  '+title[0].decode('utf-8'))
        else:
            print(url + '  ' + str(r.status_code) + '  ' + r.content.decode('utf-8').replace('\n','')[0:30])
            res.append(url + '  ' + str(r.status_code) + '  ' + r.content.decode('utf-8').replace('\n','')[0:30])
    except:
        pass
    q.put(url)

@Save_info
def Hawkeye_cidr(cidr):
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

def Get_tile_file(url,res,q):
    try:
        r=requests.get(url,headers=headers,timeout=10,verify=False)
        rule = re.compile(r'<title.*?>(.*?)</title>')
        title = rule.findall(r.content.decode('utf-8'))
        if title:
            print(url+'  '+str(r.status_code)+'  '+title[0].decode('utf-8'))
            res.append(url+'  '+str(r.status_code)+'  '+title[0].decode('utf-8'))
        else:
            print(url + '  ' + str(r.status_code) + '  ' + r.content.decode('utf-8').replace('\n','')[0:30])
            res.append(url + '  ' + str(r.status_code) + '  ' + r.content.decode('utf-8').replace('\n','')[0:30])
    except:
        # print(url + '  ' + "Error" + '  ' + " 网络故障 or 目标服务故障 or 兔子心情不好")
        # res.append(url + '  ' + "Error" + '  ' + " 网络故障 or 目标服务故障 or 兔子心情不好")
        pass
    q.put(url)

@Save_info
def Hawkeye_file(filename):
    res = Manager().list([])
    p = Pool(30)
    q = Manager().Queue()
    try:
        f=open(filename,'r')
        urls=f.readlines()
        f.close()

        print('侦测开始~加载任务量：{}条'.format(len(urls)))
        if urls:
            for i in urls:
                p.apply_async(Get_tile_file, args=(urlcheck(i.replace('\n','')),res,q))
            p.close()
            p.join()
            return res
        else:
            print("文件内容错误，锤你昂w(ﾟДﾟ)w")
    except:
        print("给我个文件吖喂 w(ﾟДﾟ)w")


def run(*args):
    if len(args)==1:
        if '/' in args[0]:
            Hawkeye_cidr(args[0])
        else:
            Hawkeye_file(args[0])


if __name__ == '__main__':
    print(Get_tile('https://github.com/rabbitmask/AssetsHunter'))
