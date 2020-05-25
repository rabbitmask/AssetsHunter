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
from Modules_Active import hawkeye
from Modules_Passive import domain_ip, crt_domain, asn_cidr, censys_ip, ip_whois, domain_whois
from Tools import cidr_ip, kill_repeat, email_dig
from Cracks import mysql_crack, redis_crack, ftp_crack, ssh_crack

aboutdic='  level 1 password 10\n  level 2 password 100\n  level 3 password 1000\n  level 4 password 10000\n  level 5 password 100000\n  level 0 From yourself! :)'


def Console():
    parser = argparse.ArgumentParser()
    ahf_modules_passive = parser.add_argument_group('AHF Modules_Passive')
    ahf_modules_active = parser.add_argument_group('AHF Modules_Active')
    ahf_tools = parser.add_argument_group('AHF Tools')
    ahf_cracks = parser.add_argument_group('AHF Cracks')


########################################################################################################################


    #被动式扫描模块
    parser.add_argument("-t", dest='target', help="target")
    parser.add_argument("-p", dest='port',help="port")
    parser.add_argument("-u", dest='user', help="user")
    parser.add_argument("-l", dest='level', help="level")

    #主动式扫描模块
    ahf_modules_active.add_argument("-hawkeye", dest='hawkeye',help="Cidr Site 侦测")

    #被动式扫描模块
    ahf_modules_passive.add_argument("-asn", dest='asn',help="ASN查询ICDR")
    ahf_modules_passive.add_argument("-censys", dest='censys',help="CENSYS API查询")
    ahf_modules_passive.add_argument("-crt", dest='crt',help="证书透明度查询域名")
    ahf_modules_passive.add_argument("-dns", dest='dns',help="DNS A记录解析")
    ahf_modules_passive.add_argument("-fofa", dest='fofa',help="FOFA API查询(待开放)")
    ahf_modules_passive.add_argument("-ipwhois", dest='ipwhois',help="IP Whois查询")
    ahf_modules_passive.add_argument("-whois", dest='whois',help="域名Whois查询")
    ahf_modules_passive.add_argument("-shadon", dest='shadon',help="Shadon API查询(待开放)")


    #资产收集工具模块
    ahf_tools.add_argument("-cidr", dest='cidr',help="Cidr转换为IP范围")
    ahf_tools.add_argument("-emaildig", dest='emaildig',help="Email挖掘工具(入口:文件)")
    ahf_tools.add_argument("-removal", dest='removal',help="数据去重工具(入口:文件)")

    #轻量级爆破模块
    ahf_cracks.add_argument("-mysqlc", dest='mysqlc',default='',help="MySQL爆破")
    ahf_cracks.add_argument("-redisc", dest='redisc', default='', help="redis爆破")
    ahf_cracks.add_argument("-ftpc", dest='ftpc', default='', help="FTP爆破")
    ahf_cracks.add_argument("-sshc", dest='sshc', default='', help="SSH爆破")

    args = parser.parse_args()


########################################################################################################################


    #主动式扫描模块
    if args.hawkeye:
        hawkeye.run(args.hawkeye)

    #被动式扫描模块
    elif args.asn:
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

    #资产收集工具模块
    elif args.cidr:
        cidr_ip.run(args.cidr)
    elif args.emaildig:
        email_dig.run(args.emaildig)
    elif args.removal:
        kill_repeat.run(args.removal)

    #轻量级爆破模块
    elif args.mysqlc:
        try:
            mysql_crack.run(args.mysqlc,args.port,args.user,args.level)
        except:
            print('eg: python AssetsHunter.py -mysqlc 127.0.0.1 -p 3306 -u root -l 1\n'+aboutdic)
    elif args.redisc:
        try:
            redis_crack.run(args.redisc,args.port,args.level)
        except:
            print('eg: python AssetsHunter.py -redisc 127.0.0.1 -p 6379 -l 1\n'+aboutdic)
    elif args.ftpc:
        try:
            ftp_crack.run(args.ftpc,args.port,args.user,args.level)
        except:
            print('eg: python AssetsHunter.py -ftpc 127.0.0.1 -p 21 -u rabbit -l 1\n'+aboutdic)
    elif args.sshc:
        try:
            ssh_crack.run(args.sshc,args.port,args.user,args.level)
        except:
            print('eg: python AssetsHunter.py -sshc 127.0.0.1 -p 22 -u rabbit -l 1\n'+aboutdic)


########################################################################################################################
