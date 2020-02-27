#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 14:43
# @Author  : tanxw
# @Desc    : 动态内容测试

import lxml.html
from lesson503.downloader import Downloader
D = Downloader()
# html = D('http://example.webscraping.com/places/default/search')
# tree = lxml.html.fromstring(html)
# data = tree.cssselect('div#result a')
# print(data)

# import json
# jsonData = D('http://example.webscraping.com/places/ajax/search.json?&search_term=A&page_size=10&page=0')
# # print(jsonData.decode('utf8'))
#
# # jsonData2 = '{"records": [{"pretty_link": "<div><a href=\\"/places/default/view/Afghanistan-1\\"><img src=\\"/places/static/images/flags/af.png\\" /> Afghanistan</a></div>", "country": "Afghanistan", "id": 5875381}, {"pretty_link": "<div><a href=\\"/places/default/view/Aland-Islands-2\\"><img src=\\"/places/static/images/flags/ax.png\\" /> Aland Islands</a></div>", "country": "Aland Islands", "id": 5875382}, {"pretty_link": "<div><a href=\\"/places/default/view/Albania-3\\"><img src=\\"/places/static/images/flags/al.png\\" /> Albania</a></div>", "country": "Albania", "id": 5875383}, {"pretty_link": "<div><a href=\\"/places/default/view/Algeria-4\\"><img src=\\"/places/static/images/flags/dz.png\\" /> Algeria</a></div>", "country": "Algeria", "id": 5875384}, {"pretty_link": "<div><a href=\\"/places/default/view/American-Samoa-5\\"><img src=\\"/places/static/images/flags/as.png\\" /> American Samoa</a></div>", "country": "American Samoa", "id": 5875385}, {"pretty_link": "<div><a href=\\"/places/default/view/Andorra-6\\"><img src=\\"/places/static/images/flags/ad.png\\" /> Andorra</a></div>", "country": "Andorra", "id": 5875386}, {"pretty_link": "<div><a href=\\"/places/default/view/Angola-7\\"><img src=\\"/places/static/images/flags/ao.png\\" /> Angola</a></div>", "country": "Angola", "id": 5875387}, {"pretty_link": "<div><a href=\\"/places/default/view/Anguilla-8\\"><img src=\\"/places/static/images/flags/ai.png\\" /> Anguilla</a></div>", "country": "Anguilla", "id": 5875388}, {"pretty_link": "<div><a href=\\"/places/default/view/Antarctica-9\\"><img src=\\"/places/static/images/flags/aq.png\\" /> Antarctica</a></div>", "country": "Antarctica", "id": 5875389}, {"pretty_link": "<div><a href=\\"/places/default/view/Antigua-and-Barbuda-10\\"><img src=\\"/places/static/images/flags/ag.png\\" /> Antigua and Barbuda</a></div>", "country": "Antigua and Barbuda", "id": 5875390}], "num_pages": 22, "error": ""}\n'
# # byte 字段解码
# jsonData2 = jsonData.decode('utf8')
# # 使用python的json模块解析成一个字典
# print(json.loads(jsonData2))

# import json
# import string
# template_url = 'http://example.webscraping.com/places/ajax/search.json?&search_term={}&page_size=10&page={}'
# countries = set()
#
# for letter in string.ascii_lowercase:
#     page = 0
#     while True:
#         html = D(template_url.format(letter, page))
#         try:
#             if html:
#                 ajax = json.loads(html.decode('utf8'))
#         except ValueError as e:
#             print(e)
#             ajax = None
#         else:
#             for record in ajax['records']:
#                 countries.add(record['country'])
#             page += 1
#             if ajax is None or page >= ajax['num_pages']:
#                 break
# open('countries.txt', 'w').write('\n'.join(sorted(countries)))


# import json
# url = 'http://example.webscraping.com/places/ajax/search.json?page=0&page_size=1000&search_term='
# jsonData = json.loads(D(url+'.').decode('utf8'))['num_pages']
# print(jsonData)

# import csv
# import json
# # FIELDS = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code', 'currency_name', 'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')
# FIELDS = ('id', 'country', 'pretty_link')
# writer = csv.writer(open('countries.csv', 'w'))
# writer.writerow(FIELDS)
# url = 'http://example.webscraping.com/places/ajax/search.json?page=0&page_size=1000&search_term=.'
# html = D(url).decode('utf8')
# ajax = json.loads(html)
# for record in ajax['records']:
#     row = [record[field] for field in FIELDS]
#     writer.writerow(row)


# pip install PySide2==5.12.0
# pip install PyQt5==5.12.0
try:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    from PySide2.QtWebEngineWidgets import *
except:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *

url = 'http://example.webscraping.com/places/default/dynamic'
# html = D(url)
# tree = lxml.html.fromstring(html)
# content = tree.cssselect('#result')[0].text
# print(content)

app = QApplication([])
webview = QWebEngineView()
webview.load(QUrl(url))
html = webview.window()
tree = lxml.html.fromstring(html)
content = tree.cssselect('#result')[0].text
print(content)
app.exit(app.exec_())



