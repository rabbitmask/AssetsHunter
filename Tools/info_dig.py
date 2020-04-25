#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
#这是一个样例轮子，并未集成进入框架
#因为敏感信息的收集更倾向于实景定制
#这里是曾经笔者用过的一个样例，留给大家参考
#其中的细节对于混乱的txt处理很有借鉴价值

import re
import time


def Info_dig(filename):
    fr=open(filename,'r')
    # fr=open(filename,'r',encoding='UTF-8')
    data=fr.readlines()
    fr.close()

    data_str=''
    for i in data:
        data_str=data_str+i.replace('\n','')

    name = re.compile(r'(姓名：.*?)帐号').findall(data_str)
    job = re.compile(r'(职务/岗位：.*?)所在部门').findall(data_str)
    department =re.compile(r'(所在部门：.*?)办公总机').findall(data_str)
    email=re.compile(r'(邮箱：.*?)分机').findall(data_str)
    phone=re.compile(r'(手机：.*?)传真电话').findall(data_str)

    timetoken = str(int(time.time()))
    filename = 'info_dig_result_{}.rabbit'.format(timetoken)

    for i in range(len(name)):
        fw=open(filename,'a')
        fw.write('No '+str(i+1)+'\n'+name[i]+'\n'+job[i]+'\n'+department[i]+'\n'+email[i]+'\n'+phone[i]+'\n\n\n')
        fw.close()
        print('结果已保存至：'+filename)


if __name__ == '__main__':
    Info_dig('demo.txt')