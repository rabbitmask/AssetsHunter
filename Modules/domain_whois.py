#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
#时间关系，我还没想好怎么玩这个. . . . . .

import whois
from Core.decorators import Print_info


def Domain_whois(domain):
    return whois.whois(domain)

def Domain_email(domain):
    return whois.whois(domain)["emails"]

def Domains_whois(domains):
    res=[]
    for i in domains:
        res.append(whois.whois(i))
    return res

def Domains_email(domains):
    res=[]
    for i in domains:
        res.append(whois.whois(i)["emails"])
    return res

@Print_info
def Domains_email_run():
    fr=open('domain.txt','r')
    domains=fr.readlines()
    fr.close()
    print(domains)
    res=[]
    for i in domains:
        res.append(whois.whois(i.replace('\n',''))["emails"])
    return res

def run(domain):
    print(Domain_whois(domain))

if __name__ == '__main__':
    res=run("www.taobao.com")
    print(res)
