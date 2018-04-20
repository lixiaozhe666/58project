# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/04/19 21:51'
from bs4 import BeautifulSoup
import  requests
import time
import pymongo

client = pymongo.MongoClient("localhost",27017)
ceshi = client.ceshi
url_list =ceshi.url_list
list_info =ceshi.list_info
# for i in url_list.find():
#     print i
def get_links_from(channel,page,whesell=1):
    # url ="http://cn.58.com/jiadian/1/pn2/"
    url ="{}{}/pn{}".format(channel,str(whesell),str(page))
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select("#infolist  div.left > a")
    if soup.find("div","business_main commonInfo"):
        for link in links:
            itemlink = link.get("href").split("?")[0]
            url_list.insert_one({"url":itemlink})
            print itemlink
    else:
        print "meiyou"


def get_list_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,"lxml")
    print soup.prettify()
    no_longer_exist = "404" in soup.find("script",type="text/javascript").get("src").split("/")
    if no_longer_exist:
        print "nolonger"
        pass
    else:
        title = soup.title.text
        price = soup.select("span.price")[0].text
        date =soup.select(".time")[0].text
        area = list(soup.select("span.c_25d > a")[0].stripped_strings) if soup.find_all("span","c_25d") else None


# get_links_from("http://cn.58.com/jiadian/",2)

get_list_info("http://cn.58.com/jiadian/336211225587")