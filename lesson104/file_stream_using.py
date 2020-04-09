#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 9:16
# @Author  : tanxw
# @Desc    : 文件流使用

import sys, time, os

# stdin 流的标准输入
# sys.stdin = open('version.txt', 'r', encoding='utf8')
# for line in sys.stdin.readlines():
#     print(line)

# stdout 流的标准输出
# sys.stdout = open('version.txt', 'a', encoding='utf8')
# print('saygoodbye')
# sys.stdout.close()

# stderr 流的标准输出
# sys.stderr = open('record.log', 'a', encoding='utf8')
# f = open(r'./version.txt', 'r', encoding='utf8')
# t = time.strftime('%Y-%m-%dX', time.localtime())
# content = f.read()
# if content:
#     sys.stderr.write(t + '\n' + content)
# else:
#     raise Exception(t + "异常信息")

# 模拟Java的输入、输出流
# 文件输入流
def FileInputStream(filename):
    try:
        f = open(filename, encoding='utf8')
        for line in f:
            for byte in line:
                yield byte
    except StopIteration as e:
        f.close()
        return

def FileOutputStream(inputStream,filename):
    try:
        f = open(filename, 'w', encoding='utf8')
        while True:
            byte = next(inputStream)
            f.write(byte)
    except StopIteration as e:
        f.close()
        return

if __name__ == '__main__':
    FileOutputStream(FileInputStream(r'./version.txt'), 'version2.txt')

# 文件处理示例-文件属性浏览程序
# def showFileProperties(path):
#     # 显示文件的属性。包括路径、大小、创建日期、最后修改时间，最后访问时间
#     for root, dirs, files in os.walk(path, True):
#         print('位置：%s' % root)
#         for filename in files:
#             state = os.stat(os.path.join(root, filename))
#             info = '文件名：' + filename + ' '
#             info += '大小：' + ('%d' % state[-4]) + ' '
#             t = time.strftime('%Y-%m-%d %X', time.localtime(state[-1]))
#             info += '创建时间：' + t + ' '
#             t = time.strftime('%Y-%m-%d %X', time.localtime(state[-2]))
#             info += '最后修改时间：' + t + ' '
#             t = time.strftime('%Y-%m-%d %X', time.localtime(state[-3]))
#             info += '最后访问时间：' + t + ' '
#             print(info)
#
# if __name__ == '__main__':
#     path = r'./'
#     showFileProperties(path)