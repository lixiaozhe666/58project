# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/04/21 13:45'
from bs4 import BeautifulSoup
import requests
import random

def cip(ip):
    try:
        if ip.keys()[0]=="http":
            requests.get('http://ip.chinaz.com/getip.aspx',proxies={'http':ip["http"]},timeout=3)
        else:
            requests.get('http://ip.chinaz.com/getip.aspx', proxies={'https': ip["https"]}, timeout=3)
    except:
        # print("failure")
        return False
    else:
        print(ip)
        return  True



def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[5].text+'://'+tds[1].text + ':' + tds[2].text)

    return ip_list



# if __name__ == '__main__':
#     url = 'http://www.xicidaili.com/nn/'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
#     }
#     ip_list = get_ip_list(url, headers=headers)
#     for ip in ip_list:
#         cip(ip)
    # proxies = get_random_ip(ip_list)
    # print(proxies)

IP_LIST ='''
    HTTP://61.135.217.7:80
    HTTPS://114.215.83.184:3128
    HTTP://122.114.31.177:808
    HTTP://123.56.89.238:60443
    HTTPS://49.79.193.138:61234
    HTTPS://183.159.93.28:18118
    HTTPS://183.159.80.14:18118
    HTTP://114.99.28.110:18118
    HTTPS://183.159.88.201:18118
    HTTPS://183.159.80.246:18118
    HTTP://49.79.193.93:61234
    HTTP://111.155.116.237:8123
    HTTPS://117.68.194.66:18118
    HTTPS://60.177.228.169:18118
    HTTPS://183.159.87.2:18118
    HTTPS://183.159.88.75:18118
    HTTP://183.159.83.235:18118
    HTTP://202.104.184.5:808
    HTTP://14.120.181.241:61234
    HTTP://14.118.254.216:6666
    HTTP://124.235.121.216:8118
    HTTPS://121.12.148.117:808
    HTTP://183.159.89.41:18118
    HTTP://183.159.94.2:18118
    HTTPS://123.134.250.205:61234
    HTTPS://182.202.220.182:61234
    HTTPS://58.60.186.249:8118
    HTTPS://183.159.92.0:18118
    HTTP://114.100.179.149:61234
    HTTPS://183.159.90.136:18118
    HTTP://183.159.94.148:18118
    HTTPS://60.177.227.17:18118
    HTTPS://110.73.34.248:8123
    HTTP://60.177.230.58:18118
    HTTP://119.115.235.131:8118
    HTTP://183.159.83.2:18118
    HTTPS://183.159.91.182:18118
    HTTPS://222.218.252.194:8118
    HTTPS://183.159.84.19:18118
    HTTP://171.115.237.29:61234
    HTTP://60.177.224.173:18118
    HTTPS://182.88.186.129:8123
    HTTPS://183.159.80.138:18118
    HTTP://183.159.87.155:18118
    HTTPS://218.72.109.166:18118
    HTTP://183.159.84.219:18118
    HTTPS://125.127.144.64:61234
    HTTPS://218.72.109.70:18118
    HTTP://183.159.95.221:18118
    HTTPS://183.159.92.211:18118
    HTTPS://119.128.172.105:8118
    HTTPS://183.159.86.7:18118
    HTTP://211.147.67.150:80
    HTTP://183.159.81.187:18118
    HTTPS://182.202.221.44:61234
    HTTPS://183.159.80.159:18118
    HTTPS://183.159.87.161:18118
    HTTPS://171.13.3.6:6666
    HTTPS://115.58.129.187:8118
    HTTPS://218.72.108.185:18118
    HTTPS://183.159.84.250:18118
    HTTPS://60.177.225.50:18118
    HTTPS://218.72.109.121:18118
    HTTPS://183.159.81.172:18118
    HTTPS://117.36.103.170:8118
    HTTP://183.159.84.204:18118
    HTTPS://183.159.91.101:18118
    HTTPS://183.159.82.208:18118
    HTTPS://117.82.227.176:8118
    HTTPS://120.36.88.58:8118
    HTTP://183.159.95.16:18118
    HTTPS://60.177.224.241:18118
    HTTPS://183.159.91.212:18118
    HTTPS://121.231.168.233:6666
    HTTPS://183.159.81.135:18118
    HTTPS://125.122.169.21:6666
    HTTPS://14.120.181.216:61234
    HTTPS://183.128.34.75:18118
    HTTPS://60.177.226.179:18118
    HTTPS://183.159.87.30:18118
    HTTP://114.221.60.9:8118
    HTTP://111.192.176.169:8118
    HTTPS://14.118.252.116:6666
    HTTP://183.159.83.73:18118
    HTTPS://183.159.84.46:18118
    HTTPS://183.159.90.160:18118
    HTTPS://183.159.92.66:18118
    HTTPS://125.127.141.88:61234
    HTTPS://117.66.134.65:8118
    HTTPS://183.159.84.60:18118
    HTTP://183.159.90.154:18118
'''
# HTTP://112.86.153.61:8118
# HTTP://110.73.28.200:8123
# HTTPS: // 60.177.227.96:18118
#HTTPS://183.159.95.174:18118
# HTTPS://60.177.231.253:18118
# HTTP://124.161.100.70:8118
# HTTP://123.53.119.69:61234
#HTTP://171.115.237.247:61234
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list.split():
        proxy_list.append( ip)
    proxy_ip = random.choice(proxy_list)
    if proxy_ip[4] == "S":
        proxies = {'https': proxy_ip}
    else:
        proxies = {'http': proxy_ip}

    return proxies

Headers='''
    Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13:
    Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 Safari/419.3:
    Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1: 
    Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3: 
    Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12 
'''
def Random_header(Headers):
    header_list = []
    for header in Headers.split(':'):
        header_list.append(header.strip())
    proxy_header = random.choice(header_list)

    return proxy_header
# cip("//119.115.235.131:8118/")
# headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
#     }
# for ip in get_ip_list('http://www.xicidaili.com/nn/1',headers=headers):
#     print(ip)
# for i in range(1,20):
#     get_random_ip(IP_LIST)
# print Random_header(Headers)