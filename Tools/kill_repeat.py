#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
from Config.config_saveinfo import Saveinfo_n


@Saveinfo_n
def Kill_repeat(filename):
    fr=open(filename,'r')
    # fr=open(filename,'r',encoding='utf-8')
    data = fr.readlines()
    fr.close()

    print("去重前：{}条数据".format(len(data)))
    data = list(set(data))
    data.sort()
    print("去重后：{}条数据".format(len(data)))
    return data

def run(filename):
    Kill_repeat(filename)


if __name__ == '__main__':
    run('demo.txt')