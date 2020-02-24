#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 18:02
# @Author  : tanxw
# @Desc    : 实现一个简单的爬虫
"""
    python3版本中,urllib,urllib2已合并，统一使用urllib模块
"""
import urllib.request
import urllib.error

def download(url, user_agent='wswp', num_retries=3):
	print('Downloading:%s',url)
	headers = {'User-agent': user_agent}
	request = urllib.request.Request(url, headers=headers)
	try:
	    html = urllib.request.urlopen(request).read()
	except urllib.error.URLError as e:
		print('Download error:', e.reason)
		html = None
		if num_retries > 0:
			if hasattr(e,'code') and 500 <= e.code < 600:
				return download(url, user_agent, num_retries-1)
	return html


print(download("http://example.webscraping.com","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",3))
