# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/04/21 10:27'
from multiprocessing import Pool
from channel_extract import ChannelList
from page_parsing import get_links_from,get_list_info,url_list
import pymongo

client = pymongo.MongoClient("localhost",27017)
ceshi = client.ceshi
none_url_list =ceshi.none_url_list
def get_all_link_from(channel):
    for num in range(1,101):
        if get_links_from(channel,num) =="meiyou":
            if(num ==1):
                none_url_list.insert_one({"channel":channel})
            break




if __name__=="__main__":
    pool = Pool()
    pool.map(get_links_from,ChannelList.split())
    urllist =[]
    for url in url_list.find():
        urllist.append(url["url"])
    pool.map(get_list_info, urllist)



