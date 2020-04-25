#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
#这个轮子是由crt.sh提供的API
#用于证书透明度=》域名查询，辅助子域名收集
import requests
from lxml import etree
from Config.config_requests import headers
from Core.decorators import Save_info


@Save_info
def Crt_domain(domain):
    req = requests.get("https://crt.sh/?q="+str(domain), headers=headers)
    domains = etree.HTML(req.text).xpath("//tr//td[5]/text()")
    domains=list(set(domains))
    domains.sort()
    return domains


def run(domain):
    Crt_domain(domain)

if __name__ == '__main__':
    run("taobao.com")

