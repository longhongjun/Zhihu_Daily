# -*- coding: utf-8 -*-
#author: Jas0ndyq
#date: 2014/9/1
#API来自izzyleung的知乎api分析


import urllib2
import re
import json

url = 'http://news-at.zhihu.com/api/3/news/latest' #提取知乎日报最新消息
content = urllib2.urlopen(url).read()
data = json.loads(content)

date = data['date'] #提取日期
a = data['top_stories'] #提取热文
b = data['stories'] #提取全部内容
count_a = len(a) 
count_b = len(b)
#print count_a
#print count_b
###确定每个字典键值对个数
print '这是' + str(date) + '的知乎日报'
print '======================================================='
print '最近：'
for i in range(int(count_a)):
    print a[i]['title']
    print a[i]['share_url']
    
print '======================================================='

print '要点：'
for i in range(int(count_b)):
	print b[i]['title']
	print b[i]['share_url']

 
