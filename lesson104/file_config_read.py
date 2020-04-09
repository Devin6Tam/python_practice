#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 23:47
# @Author  : tanxw
# @Desc    : 读取配置文件的内容

import configparser
# 读取配置
# config = configparser.ConfigParser()
# path = "config/pip.ini"
# config.read(path, encoding='utf8')
# sections = config.sections()
# print('配置块：', sections)
# for section in sections:
#     o = config.options(section)
#     print('配置项：', o)
#     v = config.items(section)
#     print('内容：', v)

# 写入配置
# config = configparser.ConfigParser()
# config.add_section('ADD_ITEM')
# config.set('ADD_ITEM', 'trusted', 'true')
# path = "config/pip.ini"
# with open(path, 'a+', encoding='utf8') as f:
#     config.write(f)
#     f.close()

# 修改配置
# config = configparser.ConfigParser()
# path = "config/pip.ini"
# config.read(path, encoding='utf8')
# config.set('ADD_ITEM', 'trusted', 'false')
# with open(path, 'r+', encoding='utf8') as f:
#     config.write(f)
#     f.close()

# 配置块，配置项删除
config = configparser.ConfigParser()
path = "config/pip.ini"
config.read(path, encoding='utf8')
config.remove_option('ADD_ITEM', 'trusted')
config.remove_section('ADD_ITEM')
with open(path, 'w+', encoding='utf8') as f:
    config.write(f)
    f.close()