#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 16:49
# @Author  : tanxw
# @Desc     : 正则表达式使用

import re

# 邮箱匹配
# ret = re.match(r'\w{4,20}', 'test@sina.com')
# print(ret)
#
# ret = re.match(r'\w{4,20}@(qq|sina|126|163)', 'test@sina.com')
# print(ret)
#
# ret = re.match(r'\w{4,20}@\w*', 'test@sina.com')
# print(ret)
#
# ret = re.match(r'\w{4,20}@\w{2,10}.(com|cn|xyz)', 'test@qq.com')
# print(ret)

# 手机，座机匹配
# ret = re.match(r'1[3-9]\d{9}', '18898750918')
# print(ret)
#
# ret = re.match(r'\d{4}-\d{7}', '0756-5574521')
# print(ret)


# 网址
# main_url_str = r'(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))'
# ret = re.match(main_url_str, 'www.baidu.com')
# print(ret)
# ret = re.match(main_url_str, '220.172.56.30')
# print(ret)
#
# param_url_str = r'(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?'
# ret = re.match(param_url_str, "/100/10")
# print(ret)
#
# complete_url_str = r'((http|ftp|https)://)?(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?'
# ret = re.match(complete_url_str, "http://www.baidu.com/aaa?pageNo=10&pageSize=10")
# print(ret)

# 中文名匹配
# ret = re.match(r'[\u4e00-\u9fa5]+', "张明明")
# print(ret.group())
#
# ret = re.match(r'.*?([\u4E00-\u9FA5]+大学)', 'study in 山东大学')
# print(ret.group())

# 多个选择项
# ret = re.match(r'(.*[0-9],)|(.*[a-zA-Z],)', "1,2,3,4,")
# print(ret.group())
#
# ret = re.match(r'(.*[0-9],)|(.*[a-zA-Z],)', "nanchang,jiujiang,ganzhuo,ji'an,shangrao,fuzhou,pingxiang,")
# print(ret.group())


# 密码
# ^ 开始
# ((\d+)|([A-Za-z]+)|(\W+)) 纯数字，字母，符号
# \d 等同于 [0-9]
# \D 等同于 [^0-9]
# \w 等同于 [0-9a-zA-Z]
# \W 等同于 [^0-9a-zA-Z]
# $ 结尾

# controll = True
# while(controll):
#     password = input("请输入密码：\n")
#     pwd_len = len(password)
#     if pwd_len >= 8 and pwd_len <= 16:
#         pass
#     else:
#         print("请输入8~16的密码")
#         continue
#
#     if re.compile('[\u4e00-\u9fa5]+').findall(password):
#         print("输入密码错误")
#         continue
#
#     ret = re.match(r'^(([0-9]+)|([A-Za-z]+)|(\W+))$', password)
#     if ret:
#         print("密码强度弱")
#         continue
#
#     ret = re.match(r'([0-9]+(\W+|\_+|[A-Za-z]+))+|([A-Za-z]+(\W+|\_+|[0-9]+))+|((\W+|\_+)+([0-9]+|\_+|[A-Za-z]+))+', password)
#     if ret and len(ret.group()) == len(password):
#         print("密码强度中等")
#         continue
#
#     ret = re.match(r'(\w+|\W+){8,16}', password)
#     if ret and len(ret.group()) == len(password):
#         print("密码很强壮")
#         controll = False
#     if(not controll):
#         break




