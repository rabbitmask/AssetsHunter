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
from Modules_Active import hawkeye, inforisk, whatcms
from Modules_Passive import domain_ip, crt_domain, asn_cidr, censys_ip, ip_whois, domain_whois
from Tools import cidr_ip, kill_repeat, email_dig


def Console():
    parser = argparse.ArgumentParser()
    ahf_modules_passive = parser.add_argument_group('AHF Modules_Passive')
    ahf_modules_active = parser.add_argument_group('AHF Modules_Active')
    ahf_tools = parser.add_argument_group('AHF Tools')


########################################################################################################################

    #主动式扫描模块
    ahf_modules_active.add_argument("-hawkeye", dest='hawkeye',help="WEB侦测(cidr/文件)")
    ahf_modules_active.add_argument("-inforisk", dest='inforisk', help="信息泄露检测")
    ahf_modules_active.add_argument("-whatcms", dest='whatcms', help="指纹识别(TideFinger)")

    #被动式扫描模块
    ahf_modules_passive.add_argument("-asn", dest='asn',help="ASN查询ICDR")
    ahf_modules_passive.add_argument("-censys", dest='censys',help="CENSYS API查询")
    ahf_modules_passive.add_argument("-crt", dest='crt',help="证书透明度查询域名")
    ahf_modules_passive.add_argument("-dns", dest='dns',help="DNS A记录解析")
    ahf_modules_passive.add_argument("-ipwhois", dest='ipwhois',help="IP Whois查询")
    ahf_modules_passive.add_argument("-whois", dest='whois',help="域名Whois查询")


    #资产收集工具模块
    ahf_tools.add_argument("-cidr", dest='cidr',help="Cidr转换为IP范围")
    ahf_tools.add_argument("-emaildig", dest='emaildig',help="Email挖掘工具(入口:文件)")
    ahf_tools.add_argument("-removal", dest='removal',help="数据去重工具(入口:文件)")

    args = parser.parse_args()


########################################################################################################################


    #主动式扫描模块
    if args.hawkeye:
        hawkeye.run(args.hawkeye)
    elif args.inforisk:
        inforisk.run(args.inforisk)
    elif args.whatcms:
        whatcms.run(args.whatcms)

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


########################################################################################################################
