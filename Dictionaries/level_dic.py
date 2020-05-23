#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
def Get_dic(filename):
    # fr=open(filename,'r')
    fr=open(filename,'r',encoding='UTF-8')
    data=fr.readlines()
    fr.close()
    return data

def Level_dic(lv):
    lv=int(lv)
    if lv==0:
        return Get_dic('Dictionaries/1.txt')
    elif lv==1:
        return Get_dic('Dictionaries/10.txt')
    elif lv==2:
        return Get_dic('Dictionaries/100.txt')
    elif lv==3:
        return Get_dic('Dictionaries/1000.txt')
    elif lv==4:
        return Get_dic('Dictionaries/10000.txt')
    elif lv==5:
        return Get_dic('Dictionaries/100000.txt')
    else:
        print('砸场子？？？')

