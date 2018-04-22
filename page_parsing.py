# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/04/19 21:51'
from bs4 import BeautifulSoup
from getIPProxy import IP_LIST,get_random_ip,cip,Random_header,Headers
from multiprocessing import Pool
import  requests
import time
import pymongo
requests.adapters.DEFAULT_RETRIES = 5 #重试连接次数
client = pymongo.MongoClient("localhost",27017)
ceshi = client.ceshi
url_list =ceshi.url_list
list_info =ceshi.list_info
none_list_info =ceshi.none_list_info
# for i in url_list.find():
#     print i

def get_links_from(channel,page=1,whesell=1):
    # url ="http://cn.58.com/jiadian/1/pn2/"
    url ="{}{}/pn{}".format(channel,str(whesell),str(page))
    proxy = get_random_ip(IP_LIST)
    GetIpCount =1

    while (not cip(proxy)) :
        print(GetIpCount)
        proxy = get_random_ip(IP_LIST)

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    header['User-Agent']=Random_header(Headers)
    s = requests.session()
    s.keep_alive = False
    wb_data =s.get(url,headers=header,proxies=proxy)



    time.sleep(5)
    soup = BeautifulSoup(wb_data.text,'lxml')
    # print(soup)
    if soup.find("div","business_main commonInfo"):
        links = soup.select("#infolist  div.left > a")
        for link in links:
            itemlink = link.get("href").split("?")[0]
            url_list.insert_one({"url":itemlink})
            print itemlink
    elif soup.find("td","t"):
        links = soup.select("td.t > a")
        for link in links:
            itemlink = link.get("href").split("?")[0]
            url_list.insert_one({"url":itemlink})
            print itemlink
    else:
        print "meiyou"
        return "meiyou"


def get_list_info(url):
    proxy = get_random_ip(IP_LIST)
    print url
    while (not cip(proxy)):
        proxy = get_random_ip(IP_LIST)

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    header['User-Agent'] = Random_header(Headers)
    print header['User-Agent']
    try:
        s = requests.session()
        s.keep_alive = False
        wb_data = s.get(url, headers=header, proxies=proxy)

        time.sleep(1)
        soup = BeautifulSoup(wb_data.text,"lxml")


        no_longer_exist =  soup.find("p", attrs={'class':'et'})

        if no_longer_exist:
            print "nolonger"
            none_list_info.insert_one({"url":url})
            pass
        else:

            title = soup.select("head > title")[0].text  if soup.find_all("title","") and soup.select("head > title").__len__()>0 else None
            price = soup.select("span.price")[0].text if soup.find_all("span","price") and soup.select("span.price ").__len__()>0 else None
            date =soup.select("li.time")[0].text if soup.find_all("li","time") and soup.select("li.time ").__len__()>0 else None

            area = list(soup.select("span.c_25d ")[0].stripped_strings) if soup.find_all("span","c_25d") and soup.select("span.c_25d ").__len__()>0 else None
            list_info.insert_one({"title":title,"price":price,"date":date,"area":area})
    except:
        time.sleep(2)
        print "error "
# get_links_from("http://cn.58.com/bijiben/1/")

# get_list_info("http://cn.58.com/pingbandiannao/33784470346431x.shtml?psid=157881960199789864354937174&entinfo=33784470346431_0&iuType=p_1&PGTID=0d305a36-008d-2671-4c21-fde8d498df95&ClickID=1")

# for url in url_list.find():
#     print url['url']
#     get_list_info(url["url"])
# print url_list.find().count()
# get_list_info("http://cn.58.com/bijibendiannao/33418625021886x.shtml")
