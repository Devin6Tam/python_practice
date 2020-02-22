#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 16:44
# @Author  : tanxw

import pymysql
# pip install pymysql
# conn=connect(参数列表)
# 例如：
# connect = pymysql.connect(
try:
    connect = pymysql.connect(
        host='192.168.43.186',
        port=3306,
        user='root',
        passwd='123456',
        db='test',
        charset='utf8'
    )

    cursor = connect.cursor()
    # 插入单条 insert into user(id,name,password) values('1','xiaoming','123456')
    # sql2 = 'insert into user(name,age,password) values(%s,%s,%s)'
    # args2 = [(u'王五',18,u'112345'),(u'赵六',21,u'258651'),(u'田七',21,u'258651')]
    #
    # cursor.executemany(sql2,args2)
    #
    # connect.commit()

    # sql3 = 'update user set password = %s where id = 1'
    # cursor.execute(sql3,'a123456')
    #
    # connect.commit()

    sql3 = 'update user set isDelete = %s where id = 1 and isDelete = 0'
    cursor.execute(sql3,1)

    connect.commit()

    sql = 'select * from user'
    cursor.execute(sql)

    print('%d hang' % (cursor.rowcount))

    for each in cursor.fetchall():
        print(each)
except Exception as e:
    print("Connection Error: " + str(e))
finally:
        connect.close()