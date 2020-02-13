#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 9:51
# @Author  : tanxw
# @Desc    : 字符串常见使用方法

# 1. 遍历
s = "hello world"
print(s)

# for char in s:
#     print(char)

# 2. 统计
s += ", hello PYTHON"

# 统计字符串的长度
print(len(s))

# 统计某一个小字符串出现的次数
print(s.count("llo"))
print(s.count("abc"))

# 统计子字符串在字符串中出现的位置
print(s.index("llo"))
# 要查找的子字符串不存在，那么会报错
# print(s.index("abc"))


# 3. 判断类型
# 这个字符串是一个空白字符
s_str = "  \t\n\r"
print(s_str.isspace())

num_str = "一千零一"
# 这种方式不能判断小数,可以判断整数
print(num_str.isdecimal())
# 不能判断中文数字,也不能判断小数
print(num_str.isdigit())
# 能够判断中文字符
print(num_str.isnumeric())

# 4. 查找和替换

# 判断是否以指定字符串开始
print(s.startswith("hello"))
print(s.startswith("Hello"))

# 判断以指定字符串结尾
print(s.endswith("world"))

# 查找指定字符串
# index 同样可以查找指定字符串
print(s.find("llo")) # 返回索引值
print(s.find("abc")) # 如果没有找到，会返回-1，表示没找到

# 替换字符串
# replace 会返回一个新字符串，不会修改原有的字符串
print(s.replace("world", "tanxw"))
print(s)

# 5. 大小写切换
print(s.upper())
print(s.lower())

# 翻转字符串中的大小写
print(s.swapcase())

# 6. 文本对齐
poem = ["\t\n春晓",
        "孟浩然",
        "春眠不觉晓\t\n",
        "处处闻啼鸟",
        "夜来风雨声",
        "花落知多少"]
for poem_str in poem:
    # strip()去除字符串中的空白字符
    # center()居中显示
    print(poem_str.strip().center(10, " "))

# 7. 拆分和链接
poem_str = "\t\n春晓\t\n\r孟浩然   \t\r春眠不觉晓\t\n处处闻啼鸟   \t\n夜来风雨声\r\n  花落知多少"
other_str = "hello world"
# 拆分字符串，拆分完成之后是一个列表
poem_list = poem_str.split()
print(poem_list)

# 合并字符串
ret = " ".join(poem_list)
print(ret)

res = other_str.split("l")
print(res)

# 8. 切片
print(s[::])
# 截取2~5 位置的字符串
print(s[2:6])
print(s[::-1])

# 字符串排序
ret2 = sorted(s)
print(" ".join(ret2))