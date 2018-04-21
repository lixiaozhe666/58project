# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/04/19 21:02'
from bs4 import BeautifulSoup
import requests

start_url ="http://cn.58.com/sale.shtml?PGTID=0d100000-008d-2b6e-7ed9-9484158bd2d4&ClickID=2"
host_url ="http://cn.58.com"
def channelList(url = start_url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    channellist = soup.select("ul.ym-submnu > li > b > a")
    for list in channellist:
        page_url = host_url+list.get("href")
        print(page_url)

# channelList()


ChannelList ='''
    http://cn.58.com/shouji/
    http://cn.58.com/tongxunyw/
    http://cn.58.com/danche/
    http://cn.58.com/diandongche/
    http://cn.58.com/fzixingche/
    http://cn.58.com/sanlunche/
    http://cn.58.com/peijianzhuangbei/
    http://cn.58.com/diannao/
    http://cn.58.com/bijiben/
    http://cn.58.com/pbdn/
    http://cn.58.com/diannaopeijian/
    http://cn.58.com/zhoubianshebei/
    http://cn.58.com/shuma/
    http://cn.58.com/shumaxiangji/
    http://cn.58.com/mpsanmpsi/
    http://cn.58.com/youxiji/
    http://cn.58.com/ershoukongtiao/
    http://cn.58.com/dianshiji/
    http://cn.58.com/xiyiji/
    http://cn.58.com/bingxiang/
    http://cn.58.com/jiadian/
    http://cn.58.com/binggui/
    http://cn.58.com/chuang/
    http://cn.58.com/ershoujiaju/
    http://cn.58.com/yingyou/
    http://cn.58.com/yingeryongpin/
    http://cn.58.com/muyingweiyang/
    http://cn.58.com/muyingtongchuang/
    http://cn.58.com/yunfuyongpin/
    http://cn.58.com/fushi/
    http://cn.58.com/nanzhuang/
    http://cn.58.com/fsxiemao/
    http://cn.58.com/xiangbao/
    http://cn.58.com/meirong/
    http://cn.58.com/yishu/
    http://cn.58.com/shufahuihua/
    http://cn.58.com/zhubaoshipin/
    http://cn.58.com/yuqi/
    http://cn.58.com/tushu/
    http://cn.58.com/tushubook/
    http://cn.58.com/wenti/
    http://cn.58.com/yundongfushi/
    http://cn.58.com/jianshenqixie/
    http://cn.58.com/huju/
    http://cn.58.com/qiulei/
    http://cn.58.com/yueqi/
    http://cn.58.com/bangongshebei/
    http://cn.58.com/diannaohaocai/
    http://cn.58.com/bangongjiaju/
    http://cn.58.com/ershoushebei/
    http://cn.58.com/chengren/
    http://cn.58.com/nvyongpin/
    http://cn.58.com/qinglvqingqu/
    http://cn.58.com/qingquneiyi/
    http://cn.58.com/chengren/
    http://cn.58.com/xiaoyuan/
    http://cn.58.com/ershouqiugou/
    http://cn.58.com/tiaozao/

'''
# ChannelList =''' http://cn.58.com/zhubaoshipin/ '''
