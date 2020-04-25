#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import json
from ipwhois import IPWhois

def Ip_rdap(ip):
    obj = IPWhois(ip)
    results = obj.lookup_rdap()
    print("asn: AS"+results["asn"])
    print("asn_cidr: "+results["asn_cidr"])
    print("asn_registry: "+results["asn_registry"])
    print("asn_country_code: "+results["asn_country_code"])
    print("asn_description: "+results["asn_description"])

def Ip_asn(ip):
    obj = IPWhois(ip)
    results = obj.lookup_rdap(depth=1)
    print(json.dumps("AS"+results["asn"]))


def Ip_whois(ip):
    obj = IPWhois(ip)
    results = obj.lookup_rdap()
    print(json.dumps(results,indent=4))


def run(ip):
    Ip_rdap(ip)

if __name__ == '__main__':
    Ip_whois('0.0.0.0')