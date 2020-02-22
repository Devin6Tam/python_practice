#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 16:49
# @Author  : tanxw
# @Desc     : 正则表达式使用

import re

# 匹配数字
# [1-9]? 匹配0个或者1个
# \d$  匹配以数字结尾
# |100 匹配结果可为100
ret = re.match(r'[1-9]?\d$|100', 'a92')  # 100
if ret:
    print(ret.group())
else:
    print('不在0-100之间')

# 匹配邮箱
# \w{4,20} 匹配4~20个 匹配字母或数字或下划线或汉字的组合字符串
# @ 固定的邮箱符号
# (qq|126|163) 匹配@符号后面的公司名称（简称）
# .com 固定的邮箱后缀
ret = re.match(r'\w{4,20}@(qq|sina|126|163).com', 'test@sina.com')
print(ret.group())


# 匹配网址
# ((http|ftp|https)://)?   圆括号左右分组, 匹配0个或1个(http|ftp|https)://
# (([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))
# (:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?  [] 匹配任意的字符
# .com 固定的邮箱后缀
ret = re.match(r'(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))', 'www.baidu.com')
print(ret.group())
ret = re.match(r'(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?', '/')
print(ret.group())
ret = re.match(r'((http|ftp|https)://)?(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?', 'http://www.baidu.com/aaa?pageNo=10&pageSize=10')
print(ret.group())


# 匹配网页元素
labels = ['<html><h2>www.mzbloc.com</h2></html>', '<html><h1>www.mzbloc.com</h2></html>']
for label in labels:
    ret = re.match(r'<(\w*)><(\w*)>.*</\2></\1>', label)
    if ret:
        print("%s 符合要求" % ret.group())
    else:
        print("%s不符合要求" % label)
for label in labels:
    ret = re.match(r'<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>', label)
    if ret:
        print(ret.group())


# re高级用法
# search
ret = re.search(r'(\d+).*(\d+)', "阅读次数为 5666, 点赞次数: 7000")
print(ret.group(1))
print(ret)

# find 查找
ret = re.findall(r'\d+', '阅读次数为 5666, 点赞次数: 7000')
print(ret)

#sub 替换
ret = re.sub(r'\d+', '555', 'python=666')
print(ret)

# 贪婪与非贪婪
s = 'this is a number 123-123-344-333'
r = re.match(r'.+?(\d+-\d+-\d+-\d+)', s)
print(r.group(1))


s = 'c:\\a\\b\\c'
print(s)
# ret = re.match('c:\\\\a', s).group()
ret = re.match(r'c:\\a', s).group()
print(ret)