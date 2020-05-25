#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
# 借助第三方库写的A记录解析轮子
# 提供了一个对外接口，智能匹配输入类型
# 自动识别请求域名列表还是单域名类型
# 其实为了防手残还增加了`http://`和`https://`即`/`的过滤

import dns.resolver
from Core.decorators import Print_info


def Domain_ip(domain):
    res=[]
    domain=domain.replace('https://','').replace('https//','').replace('/','')
    A = dns.resolver.query(domain, 'A')
    for i in A.response.answer:
        for j in i.items:
            if j.rdtype == 1:
                res.append(j.address)
    return res



def Domains_ip(domains):
    res=[]
    for domain in domains:
        domain = domain.replace('https://', '').replace('https//', '').replace('/', '')
        A = dns.resolver.query(domain, 'A')
        for i in A.response.answer:
            for j in i.items:
                if j.rdtype == 1:
                    res.append(j.address)
    return res

@Print_info
def run(domain):
    if isinstance(domain,str):
        return Domain_ip(domain)
    elif isinstance(domain,list):
        return Domains_ip(domain)
    else:
        pass

if __name__ == '__main__':
    # print(Domain_ip("www.taobao.com"))
    # print(Domains_ip(["www.taobao.com"]))
    print(run("taobao.com"))