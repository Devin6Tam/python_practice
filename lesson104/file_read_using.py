#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 22:33
# @Author  : tanxw
# @Desc    : 文件读写
import os

# mode = 'r' 读取文件内容
# mode = 'w' 写入文件内容
# mode = 'a' 追加写入文件内容
f = open("version.txt", 'r', encoding="utf8")


# 读取单行内容 f.readline()
# 读取固定空间的内容 f.readline(1024) 1kb = 1024 字符
# 读取所有行内容 f.readlines(),f.read()
while True:
    text = f.readline()
    if not text:
        break
    print(text, end="")

f.close()
######################################################################
# 文件改名
# os.rename("demo7.txt","demo8.txt")

# 文件删除
# os.remove("demo8.txt")

# 创建文件夹(目录)
os.mkdir("今天好开心")

# 删除文件夹(目录)
# os.rmdir("今天好开心")
######################################################################

# 创建文件夹  makedirs 多可以是多层目录
path = "ppl"
if not os.path.exists(path):
    os.makedirs(path)

######################################################################

# 文件写入
f2 = open(path+"/aaa.txt", 'a', encoding="utf8")
# f2.write("从前有座山，山上有座庙，庙里有个老和尚，老和尚说,\"从前有座山\"")
f2.write("从前有座山，山上有座庙，庙里有个老和尚，老和尚说,\"从前有座山...\"\n")
f2.close()

# 文件写入（简易代码）
with open(path+"/ccc.txt", 'a', encoding='utf8') as f:
    f.write("床前明月光，疑是地上霜。举头望明月，低头思故乡 -- 李白  《望月》 \n")

######################################################################

# 小文件复制
f3 = open(path+"/aaa.txt", "r", encoding="utf8")
f4 = open(path+"/bbb.txt", "w", encoding="utf8")
f3_text = f3.read()
f4.write(f3_text)

######################################################################

# 大文件复制
f3 = open(path+"/aaa.txt", "r", encoding="utf8")
f4 = open(path+"/bbb.txt", "w", encoding="utf8")
while True:
    text = f3.readline()
    if not text:
        break
    print(text, end="")
f4.write(f3_text)
