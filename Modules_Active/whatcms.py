#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import hashlib
import json
import requests
from Config.config_requests import headers


def getmd5(hash):
    md5 = hashlib.md5()
    md5.update(hash)
    return md5.hexdigest()

def md5_check(url,path,match_pattern,cms_name):
    try:
        r = requests.get(url+path, headers=headers, timeout=3, verify=False)
        if match_pattern == getmd5(r.content):
            return cms_name
    except:
        pass


def keyword_check(url,path,match_pattern,cms_name):
    try:
        r = requests.get(url+path, headers=headers, timeout=3, verify=False)
        if match_pattern in r.text:
            return cms_name
    except:
        pass



def Whatcms(url):
    fr = open('Dictionaries/TideFinger.json','r', encoding='UTF-8')
    data= json.load(fr, encoding='utf-8')
    fr.close()
    print('指纹加载成功：{}条'.format(len(data)))
    print('Power By Tidefinger：http://finger.tidesec.com')
    for i in data:
        if i['options']=='md5':
            res=md5_check(url,i['path'],i['match_pattern'],i['cms_name'])
            if res:
                print('目标指纹：'+res)
                break
        elif i['options']=='keyword':
            res=keyword_check(url,i['path'],i['match_pattern'],i['cms_name'])
            if res:
                print('目标指纹：'+res)
                break
        else:
            print('快康康我！我好像傻啦w(ﾟДﾟ)w')



def run(url):
    Whatcms(url)

if __name__ == '__main__':
    run('http://127.0.0.1')