#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
#Hello~又是轮子时间，此模块提供了三个方法
#Censys_ip用于框架调度，默认只查一页（100条）
#Censys_ip_all是留给小伙伴们手动调度的轮子彩蛋
#Censys_demo为最原始Demo，方便小伙伴们进行其他调度使用
#请放心使用，异常精确制停将不会浪费您的API次数
#模块更新时间：2020年4月24日00点14分 状态：已验收

import json
from time import sleep
import requests
from Config.config_censys import API_ID, API_SECRET, API_URL
from Config.config_requests import headers
from Core.decorators import  Save_info


@Save_info
def Censys_ip(Domain,page):
    data = {
        "query": Domain,
        "page": page,
        "fields": ["ip"],
    }
    try:
        res = requests.post(API_URL,data=json.dumps(data), auth=(API_ID, API_SECRET),headers=headers)
        results=res.json()["results"]
        ips=[]
        for i in results:
            ips.append(i["ip"])
        return ips
    except:
        print("Censys访问网络故障...")


def Censys_ip_all(Domain):
    ips=[]
    i=1
    while 1:
        res=Censys_ip(Domain,i)
        if res:
            ips=ips+res
            if len(res)<100:
                break
            i=i+1
            sleep(1)
        else:
            print("这可能是一份不完整的结果...")
            break
    return ips


def Censys_demo(Domain):
    data = {
        "query": Domain,
        "page": 1,
        "fields": [],
    }
    res = requests.post(API_URL,data=json.dumps(data), auth=(API_ID, API_SECRET),headers=headers)
    return res.json()

def run(Domain):
    return Censys_ip(Domain, 1)


if __name__ == '__main__':
    print(Censys_ip("taobao.com",1))
    # print(Censys_ip_all("taobao.com"))
