#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import ipaddress
import netaddr

from Core.decorators import Print_info


def Cidr_ipc(cidr):
    ips = ipaddress.ip_network(cidr)
    return ('%s-%s' % (ips[0], ips[-1]))

def Cidr_ips(cidr):
    ips=[]
    for ip in ipaddress.IPv4Network(cidr):
        ips.append('%s'%ip)
    return ips


def Ip_cidr(startip,endip):
    cidrs = netaddr.iprange_to_cidrs(startip, endip)
    iplist=[]
    for k, v in enumerate(cidrs):
        iplist.append('%s'%v)
    return iplist

@Print_info
def run(cidr):
    return Cidr_ipc(cidr)

if __name__ == '__main__':
    print(Cidr_ips("192.168.1.1/21"))
    print(Ip_cidr('192.168.0.1', '192.169.255.255'))
