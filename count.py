# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/04/21 10:32'
from page_parsing import url_list
import  re
import time
for u in url_list.find({'students.comments':re.compile('http://cn.58.com/yishu')}):
    print u
# print url_list.find().count()