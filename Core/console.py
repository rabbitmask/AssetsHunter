#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import argparse
from Modules import domain_ip, crt_domain, asn_cidr, censys_ip, ip_whois, domain_whois
from Tools import cidr_ip, kill_repeat, email_dig


def Console():
    parser = argparse.ArgumentParser()
    ahf_modules = parser.add_argument_group('AHF Modules')
    ahf_tools = parser.add_argument_group('AHF Tools')


    ahf_modules.add_argument("-asn", dest='asn',help="ASN查询ICDR")
    ahf_modules.add_argument("-censys", dest='censys',help="CENSYS API查询")
    ahf_modules.add_argument("-crt", dest='crt',help="证书透明度查询域名")
    ahf_modules.add_argument("-dns", dest='dns',help="DNS A记录解析")
    ahf_modules.add_argument("-fofa", dest='fofa',help="FOFA API查询(待开放)")
    ahf_modules.add_argument("-ipwhois", dest='ipwhois',help="IP Whois查询")
    ahf_modules.add_argument("-whois", dest='whois',help="域名Whois查询")
    ahf_modules.add_argument("-shadon", dest='shadon',help="Shadon API查询(待开放)")

    ahf_tools.add_argument("-cidr", dest='cidr',help="Cidr转换为IP范围")
    ahf_tools.add_argument("-emaildig", dest='emaildig',help="Email挖掘工具(入口:文件)")
    ahf_tools.add_argument("-removal", dest='removal',help="数据去重工具(入口:文件)")

    args = parser.parse_args()

    if args.asn:
        asn_cidr.run(args.asn)
    elif args.crt:
        crt_domain.run(args.crt)
    elif args.censys:
        censys_ip.run(args.censys)
    elif args.dns:
        domain_ip.run(args.dns)
    elif args.ipwhois:
        ip_whois.run(args.ipwhois)
    elif args.whois:
        domain_whois.run(args.whois)
    elif args.cidr:
        cidr_ip.run(args.cidr)
    elif args.emaildig:
        email_dig.run(args.emaildig)
    elif args.removal:
        kill_repeat.run(args.removal)