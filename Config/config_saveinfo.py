#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
def Saveinfo(result):
    for i in result:
        fw=open('log.txt','a')
        fw.write(i+'\n')
        fw.close()

def Saveinfo_n(result):
    for i in result:
        fw=open('log.txt','a')
        fw.write(i)
        fw.close()