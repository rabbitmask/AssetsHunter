#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
#这里是一个邮箱挖掘机！
#输入格式为文件名，结果自动保存。

import re
from Core.decorators import Save_info

@Save_info
def Emain_dig(filename):
    fr=open(filename,'r')
    # fr=open(filename,'r',encoding='UTF-8')
    data=fr.readlines()
    fr.close()
    data_str=''
    for i in data:
        data_str=data_str+i.replace('\n','')
    print(data_str)
    rule = re.compile(r'([0-9a-zA-Z_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')
    # rule = re.compile(r'([0-9a-zA-Z_.+-]+@qq.com)')
    res = rule.findall(data_str)
    res=list(set(res))
    res.sort()
    print("捕获邮箱数量：{}".format(len(res)))
    return res


def run(filename):
    Emain_dig(filename)

if __name__ == '__main__':
    Emain_dig('demo.txt')