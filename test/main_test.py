#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql             #使用pymysql板块    

name = input("请输入名字")
pwd = input("请输入密码")
def loca():
    conn = pymysql.connect(     
        host = '127.0.0.1',     
        user='smile',            
        password='1234',          
        database='python',            
        port= 3306,      #端口号       
        charset='utf8'   #字符数
        )                       
    #e：打印数据库的错误原因  ,try检测异常
    cursor = conn.cursor()   #使用cursor方式创建一个游标
    sql = "select * from student"  #查询用户表
    cursor.execute(sql)   #查询到sql语句a
    rew = cursor.fetchone()   #fetchone获取一个结果给rew
    print(rew)
    print(sql)  #返回用户表
    ret = cursor.execute(sql)
    if ret:
        print("登陆成功")
        print(ret)
    else:
        print("登陆失败")
    cursor.close()
    conn.close()
    sql = cursor.fetchall()
loca()


print("----------------")
