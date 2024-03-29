# AssetsHunter
资产狩猎框架-AssetsHunter，信息收集是一项艺术~

```
   _____                        __           ___ ___               __
  /  _  \   ______ ______ _____/  |_  ______/   |   \ __ __  _____/  |_  ___________
 /  /_\  \ /  ___//  ___// __ \   __\/  ___/    ~    \  |  \/    \   __\/ __ \_  __ \
/    |    \\___ \ \___ \\  ___/|  |  \___ \\    Y    /  |  /   |  \  | \  ___/|  | \/
\____|__  /____  >____  >\___  >__| /____  >\___|_  /|____/|___|  /__|  \___  >__|
        \/     \/     \/     \/          \/       \/            \/          \/

                                         AssetsHunterFramework | By Tide_RabbitMask | V 1.2

usage: AssetsHunter.py [-h] [-hawkeye HAWKEYE] [-inforisk INFORISK] [-whatcms WHATCMS] [-asn ASN] [-censys CENSYS] [-crt CRT] [-dns DNS]
                       [-ipwhois IPWHOIS] [-whois WHOIS] [-cidr CIDR] [-emaildig EMAILDIG] [-removal REMOVAL]

optional arguments:
  -h, --help          show this help message and exit

AHF Modules_Passive:
  -asn ASN            ASN查询ICDR
  -censys CENSYS      CENSYS API查询
  -crt CRT            证书透明度查询域名
  -dns DNS            DNS A记录解析
  -ipwhois IPWHOIS    IP Whois查询
  -whois WHOIS        域名Whois查询

AHF Modules_Active:
  -hawkeye HAWKEYE    WEB侦测(cidr/文件)
  -inforisk INFORISK  信息泄露检测
  -whatcms WHATCMS    指纹识别(TideFinger)

AHF Tools:
  -cidr CIDR          Cidr转换为IP范围
  -emaildig EMAILDIG  Email挖掘工具(入口:文件)
  -removal REMOVAL    数据去重工具(入口:文件)

```
```
V 1.1更新日志
   新增Cracks轻量级爆破模块
      目前支持mysql、redis、ftp、ssh
   新增字典模块
      来自TideSec内部字典权重池
   原核心模块降级为被动式信息收集模块
   新增主动式信息收集模块
      Hawkeye区段快速侦测模块
      inforisk信息泄露检测模块
      whatcms指纹识别模块(TideFinger提供指纹库支持)
   修复某些不可描述的Bug
V 1.2更新日志
   移除爆破模块
   Hawkeye区段快速侦测模块增加列表文件探测支持
   更换随机UA头方案，移除fake_useragent库
```
  V 1.0说明
  https://www.jianshu.com/p/aec51e4c368e
  
  V 1.1说明
  https://www.jianshu.com/p/e87b5d2aa793
