# AssetsHunter
资产狩猎框架-AssetsHunter，信息收集是一项艺术~

```
   _                _                           _
  /_\  ___ ___  ___| |_ ___   /\  /\_   _ _ __ | |_ ___ _ __
 //_\\/ __/ __|/ _ \ __/ __| / /_/ / | | | '_ \| __/ _ \ '__|
/  _  \__ \__ \  __/ |_\__ \/ __  /| |_| | | | | ||  __/ |
\_/ \_/___/___/\___|\__|___/\/ /_/  \__,_|_| |_|\__\___|_|

                                         AssetsHunterFramework | By RabbitMask | V 1.0

usage: AssetsHunter.py [-h] [-asn ASN] [-censys CENSYS] [-crt CRT] [-dns DNS]
                       [-fofa FOFA] [-ipwhois IPWHOIS] [-whois WHOIS]
                       [-shadon SHADON] [-cidr CIDR] [-emaildig EMAILDIG]
                       [-removal REMOVAL]

optional arguments:
  -h, --help          show this help message and exit

AHF Modules:
  -asn ASN            ASN查询ICDR
  -censys CENSYS      CENSYS API查询
  -crt CRT            证书透明度查询域名
  -dns DNS            DNS A记录解析
  -fofa FOFA          FOFA API查询(待开放)
  -ipwhois IPWHOIS    IP Whois查询
  -whois WHOIS        域名Whois查询
  -shadon SHADON      Shadon API查询(待开放)

AHF Tools:
  -cidr CIDR          Cidr转换为IP范围
  -emaildig EMAILDIG  Email挖掘工具(入口:文件)
  -removal REMOVAL    数据去重工具(入口:文件)
```

  V1.0开放测试，为了增加功能并未拓展并发性
  如有bug纯属正常，有功能和API建议欢迎提议~

  说明书V1.0
  https://www.jianshu.com/p/aec51e4c368e
